from src.data_presentation.ohlcv_loader import load, plot_close_price
from preprocessing.resample import resample_to_daily,  resample_to_hourly, resample_to_weekly
from preprocessing.heikin_ashi import heikin_ashi_multiple, heikin_ashi
from src.data_presentation.candle_stick import pltCandleStick
from src.data.stock_data_manager import StockDataManager
from preprocessing.hybrid_tokenizer import hybrid_tokenize, plot_return_token_distribution, compute_pct_change
import pandas as pd

stock_files = {
    "NTPC": "data/raw/NTPC_minute.csv",
    "BHEL": "data/raw/BHEL_minute.csv",
    "RELIANCE": "data/raw/RELIANCE_minute.csv",
    "ABB": "data/raw/ABB_minute.csv",
    "ADANIENSOL": "data/raw/ADANIENSOL_minute.csv",
    "ADANIGREEN": "data/raw/ADANIGREEN_minute.csv",
    "ADANIPOWER": "data/raw/ADANIPOWER_minute.csv",
    "ADANIPORTS": "data/raw/ADANIPORTS_minute.csv",
    # Add the rest of your 87 stock symbols...
}

manager = StockDataManager(stock_files.items())




#pltCandleStick(df)
"""
#pltCandleStick(df)
df = hybrid_tokenize(df)
print("Hybrid Tokenization...")

plot_return_token_distribution(df)

df = heikin_ashi_multiple(df, 1)
df = hybrid_tokenize(df)
plot_return_token_distribution(df)"""

from src.correlation_plotter import CorrelationPlotter

combined = pd.concat([manager.get_data('NTPC')[['return_token']], manager.get_data('BHEL')[['return_token']], manager.get_data('RELIANCE')[['return_token']], manager.get_data('ABB')[['return_token']], manager.get_data('ADANIENSOL')[['return_token']], manager.get_data('ADANIGREEN')[['return_token']], manager.get_data('ADANIPOWER')[['return_token']], manager.get_data('ADANIPORTS')[['return_token']]], axis=1)
combined.columns = ['NTPC', 'BHEL', 'RELIANCE', 'ABB', 'ADANIENSOL', 'ADANIGREEN', 'ADANIPOWER', 'ADANIPORTS']
plotter = CorrelationPlotter()
plotter.plot(combined)