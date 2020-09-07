import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from strategies.strategy import Strategy

"""Moving Average Crossover algorithm.

This algorithm buys apple once its short moving average crosses
its long moving average (indicating upwards momentum) and sells
its shares once the averages cross again (indicating downwards
momentum).

Trading Rules:
-------------
Go long when SMA(N) > SMA(M) on a given day (T) and SMA(N) < SMA(M) on the previous day(T-1)
Go short when SMA(N) < SMA(M) on a given day and SMA(N) > SMA(M) on the previous day

"""

class MovingAverageCrossOverStrategy(Strategy):

    def __init__(self, symbol, bars, short_window=100, long_window=400):
        self.symbol = symbol
        self.bars = bars

        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self):
        
        # long, short or hold (1, -1 or 0)
        signals = pd.DataFrame(index=self.bars.index)
        smaT = f'SMA_{self.short_window}'
        smaTMinus1 = f'SMA_{self.short_window}_T-1'
        lmaT = f'LMA_{self.long_window}'
        lmaTMinus1 = f'LMA_{self.long_window}_T-1'
        signalColumn = f'Signal_{self.short_window}_{self.long_window}'
        signals[signalColumn] = 0.0


        signals[smaT] = self.bars['AdjClose'].rolling(window=self.short_window, center=False).mean()
        signals[lmaT] = self.bars['AdjClose'].rolling(window=self.long_window, center=False).mean()

        signals[smaTMinus1] = self.bars['AdjClose'].rolling(window=self.short_window, center=False).mean().shift(1)
        signals[lmaTMinus1] = self.bars['AdjClose'].rolling(window=self.long_window, center=False).mean().shift(1)

        # Create a 'signal' (invested or not invested), but only for the period greater than
        #  the shortest moving average window.
        signals[signalColumn][self.short_window:] = np.where((signals[smaT][self.short_window:] 
            > signals[lmaT][self.short_window:]) & (signals[smaTMinus1][self.short_window:] 
            < signals[lmaTMinus1][self.short_window:]), 1.0, 0.0)   

        signals[signalColumn][self.short_window:] = np.where((signals[smaT][self.short_window:] 
            < signals[lmaT][self.short_window:]) & (signals[smaTMinus1][self.short_window:] 
            > signals[lmaTMinus1][self.short_window:]), -1.0, signals[signalColumn])

        # Take the difference of the signals in order to generate actual trading orders
        # positions have been shifted by 1 time-step, which is done to avoid look-ahead bias 
        signals['positions'] = signals[signalColumn].shift(1)

        return signals
