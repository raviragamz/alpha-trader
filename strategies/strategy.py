"""
The Strategy class receives a Pandas DataFrame of bars, i.e. a list of Open-High-Low-Close-Volume (OHLCV) data
points at a particular frequency. The Strategy will produce a list of signals, which consist of a timestamp 
and an element from the set {1, 0, -1}  indicating a long, hold or short signal respectively.

Abstract Base class for inherited strategies - mean-reversion, momentum and volatility strategies.
"""
from abc import ABCMeta, abstractmethod

class Strategy(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_signals(self):
        """An implementation is required to return the DataFrame of symbols 
        containing the signals to go long, short or hold (1, -1 or 0)."""
        raise NotImplementedError("Should implement generate_signals()!")
