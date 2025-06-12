import pandas as pd
from preprocessing.hybrid_tokenizer import hybrid_tokenize, compute_pct_change
from preprocessing.resample import resample_to_daily, resample_to_hourly, resample_to_weekly
from preprocessing.heikin_ashi import heikin_ashi_multiple, heikin_ashi

class StockDataManager:
    data_store = {}

    def __init__(self, stock_symbol):
        for symbol,path in stock_symbol:
            if symbol not in self.data_store:
                StockDataManager.load_data(symbol, path)

    @staticmethod
    def load_data(stock_symbol, file_path):
        if stock_symbol not in StockDataManager.data_store:
            print(f"Loading data for {stock_symbol} from {file_path}")
            df = pd.read_csv(file_path, index_col='date', parse_dates=True)
            df.sort_values(by='date', inplace=True)
            df.reset_index(inplace=True)
            df['idx'] = df.index
            df = resample_to_daily(df)
            df = heikin_ashi(df)
            df = hybrid_tokenize(df)
            StockDataManager.data_store[stock_symbol] = df
        else:
            print(f"Data for {stock_symbol} already loaded.")
    
    def get_data(self, stock_symbol):
        if stock_symbol in StockDataManager.data_store:
            return StockDataManager.data_store[stock_symbol]
        else:
            raise ValueError(f"Data for {stock_symbol} not found. Please load the data first.")

    def get_all_data(self):
        return StockDataManager.data_store
    
    def get_data_for_month(self, stock_symbol, month, year):
        """
        Get stock data for a particular month.
        
        Parameters:
        -----------
        stock_symbol : str
            The stock symbol to get data for
        month : int or str
            The month to filter by (1-12 or month name like 'January')
        year : int
            The year to filter by.

        Returns:
        --------
        pd.DataFrame
            Filtered DataFrame containing only data for the specified month
        """
        if stock_symbol not in self.data_store:
            raise ValueError(f"Data for {stock_symbol} not found. Please load the data first.")
            
        df = self.data_store[stock_symbol].copy()
        
        # Convert month name to number if needed
        if isinstance(month, str):
            month_dict = {
                'january': 1, 'february': 2, 'march': 3, 'april': 4,
                'may': 5, 'june': 6, 'july': 7, 'august': 8,
                'september': 9, 'october': 10, 'november': 11, 'december': 12
            }
            month = month_dict.get(month.lower())
            if month is None:
                raise ValueError(f"Invalid month name: {month}")
        
        # Filter by month (and year if provided)
        if year is not None:
            return df[(df['date'].dt.month == month) & (df['date'].dt.year == year)]
        else:
            return df[df['date'].dt.month == month]