# You can create cells on a Python file by typing "#%%" 

class FinancialDataReader(object):
    
     def __init__(self):
         self.supported_data_providers = ("yahoo","quandl") 
         print("This is base class for reading financial data from various providers")