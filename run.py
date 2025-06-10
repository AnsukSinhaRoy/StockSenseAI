from src.data_loader.ohlcv_loader import load, plot_close_price
from src.data_loader.resample import resample_to_daily, resample_to_weekly, resample_to_hourly
from src.heikin_ashi import heikin_ashi_multiple, heikin_ashi
from src.data_loader.candle_stick import pltCandleStick

from src.tokenizer.hybrid_tokenizer import hybrid_tokenize, plot_return_token_distribution

df = load("data/raw/NTPC_minute.csv")

df = resample_to_daily(df)

#pltCandleStick(df)

df = heikin_ashi_multiple(df, 6)

#pltCandleStick(df)

print("Hybrid Tokenization...")

df = hybrid_tokenize(df)
plot_return_token_distribution(df)