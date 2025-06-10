from src.data_loader.ohlcv_loader import load_ohlcv_data, plot_close_price, resample_to_daily, resample_to_weekly, resample_to_hourly, generate_candlestick_data, plot_candlestick

from src.heikin_ashi import heikin_ashi
df = load_ohlcv_data("data/raw/NTPC_minute.csv")
#df = df[:10000]

#plot_close_price(df)


#df = resample_to_hourly(df)
#plot_close_price(df)
df = resample_to_daily(df)
#plot_candlestick(generate_candlestick_data(df))
#plot_close_price(df)
#plot_candlestick(generate_candlestick_data(df))
#df = resample_to_weekly(df)
#plot_close_price(df)
#plot_candlestick(generate_candlestick_data(df))

df = heikin_ashi(df)
df = heikin_ashi(df)
df = heikin_ashi(df)
df = heikin_ashi(df)
df = heikin_ashi(df)
df = heikin_ashi(df)


plot_candlestick(generate_candlestick_data(df))