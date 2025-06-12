import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



def load(filepath):
    print("Loading OHLCV data from:", filepath)
    df = pd.read_csv(filepath, parse_dates=['date'])
    df.sort_values('date', inplace=True)
    df.reset_index(drop=True, inplace=True)
    df['idx'] = df.index

    print ("Data loaded successfully.")
    return df



def plot_close_price(df):
    
    print("Plotting close price over time...")
    plt.figure(figsize=(14, 5))
    plt.plot(df['idx'], df['close'], label='Close Price', color='blue')
    plt.title('Close Price Over Time')
    plt.xlabel('idx')
    plt.ylabel('Close Price')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()
    print("Close price plot completed.")



