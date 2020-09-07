from financial_datareader import FinancialDataReader
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web

class PandasYahooReader(FinancialDataReader):
    
         def __init__(self, symbol):
             self.symbol = symbol
             self.provider = "yahoo"
             print("This is a child class for reading financial data from Yahoo!")

         def read(self, start, end):
            self.raw_data = web.DataReader(self.symbol, self.provider, start, end)
            symbol_file = f'{self.symbol}.csv'
            self.raw_data.to_csv(symbol_file)
            self.data = pd.read_csv(symbol_file, parse_dates = [0])

