from src.data_loader.ohlcv_loader import load, plot_close_price
from src.data_loader.resample import resample_to_daily,  resample_to_hourly, resample_to_weekly
from src.heikin_ashi import heikin_ashi_multiple, heikin_ashi
from src.data_loader.candle_stick import pltCandleStick

from src.tokenizer.hybrid_tokenizer import hybrid_tokenize, plot_return_token_distribution, compute_pct_change
import pandas as pd

data1 = load("data/raw/NTPC_minute.csv")
data1 = resample_to_weekly(data1)
data1= heikin_ashi(data1)
data1 = hybrid_tokenize(data1)

data2 = load("data/raw/BHEL_minute.csv")
data2 = resample_to_weekly(data2)
data2 = heikin_ashi(data2)
data2 = hybrid_tokenize(data2)

data3 = load("data/raw/RELIANCE_minute.csv")
data3 = resample_to_weekly(data3)
data3 = heikin_ashi(data3)
data3 = hybrid_tokenize(data3)

data4 = load("data/raw/ABB_minute.csv")
data4 = resample_to_weekly(data4)
data4 = heikin_ashi(data4)
data4 = hybrid_tokenize(data4)

data5 = load("data/raw/ADANIENSOL_minute.csv")
data5 = resample_to_weekly(data5)
data5 = heikin_ashi(data5) 
data5 = hybrid_tokenize(data5)

data6 = load("data/raw/ADANIGREEN_minute.csv")
data6 = resample_to_weekly(data6)
data6 = heikin_ashi(data6)
data6 = hybrid_tokenize(data6)

data7 = load ("data/raw/ADANIPOWER_minute.csv")
data7 = resample_to_weekly(data7)
data7 = heikin_ashi(data7)
data7 = hybrid_tokenize(data7)

data8 = load("data/raw/ADANIPORTS_minute.csv")
data8 = resample_to_weekly(data8)
data8 = heikin_ashi(data8)
data8 = hybrid_tokenize(data8)




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

combined = pd.concat([data1[['return_token']], data2[['return_token']], data3[['return_token']], data4[['return_token']], data5[['return_token']], data6[['return_token']], data7[['return_token']], data8[['return_token']]], axis=1)
combined.columns = ['NTPC', 'BHEL', 'RELIANCE', 'ABB', 'ADANIENSOL', 'ADANIGREEN', 'ADANIPOWER', 'ADANIPORTS']
plotter = CorrelationPlotter()
plotter.plot(combined)