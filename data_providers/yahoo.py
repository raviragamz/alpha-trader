from financial_datareader import FinancialDataReader

class PandasYahooReader(FinancialDataReader):
    
         def __init__(self):
            print("This is a child class for reading financial data from Yahoo!")