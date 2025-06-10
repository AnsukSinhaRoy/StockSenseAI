import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



def load_ohlcv_data(filepath):
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

def plot_candlestick(candle_data, figsize=(14, 6)):
    
    print("Plotting candlestick chart...")
    if not candle_data:
        raise ValueError("No candle data provided for plotting.")
    
    fig, ax = plt.subplots(figsize=figsize)
    width = 0.6  # width of the candlestick bodies in index units
    
    for candle in candle_data:
        # Wick (vertical line from low to high)
        ax.plot([candle['x_pos'], candle['x_pos']], 
                [candle['low'], candle['high']], 
                color='black', linewidth=1)
        
        # Candle body (rectangle between open and close)
        ax.add_patch(
            plt.Rectangle(
                (candle['x_pos'] - width/2, min(candle['open'], candle['close'])),
                width,
                abs(candle['close'] - candle['open']),
                color=candle['color'],
                linewidth=1
            )
        )

    # Set x-axis formatting
    x_positions = [candle['x_pos'] for candle in candle_data]
    date_labels = [candle['date'] for candle in candle_data]
    
    ax.set_xticks(x_positions)
    ax.set_xticklabels(date_labels, rotation=45)
    
    plt.title('Candlestick Chart')
    plt.xlabel('Index (with date labels)')
    plt.ylabel('Price')
    plt.tight_layout()
    plt.grid(True)
    plt.show()
    print("Candlestick chart plotted successfully.")


def generate_candlestick_data(df):
    print("Generating candlestick data...")
    
    if 'idx' not in df.columns:
        raise ValueError("Expected 'idx' column in DataFrame.")
    
    candle_data = []
    for _, row in df.iterrows():
        candle = {
            'x_pos': row['idx'],
            'open': row['open'],
            'high': row['high'],
            'low': row['low'],
            'close': row['close'],
            'color': 'green' if row['close'] >= row['open'] else 'red',
            'date': row['date'].strftime('%Y-%m-%d') if hasattr(row['date'], 'strftime') else str(row['date'])
        }
        candle_data.append(candle)
    
    print("Candlestick data generated successfully.")
    return candle_data


def resample_to_daily(df):
    if 'date' not in df.columns:
        raise ValueError("Expected 'date' column in DataFrame.")
    
    print("Resampling data to daily frequency...")
    # Make a copy to avoid SettingWithCopyWarning
    df = df.copy()
    
    # Drop idx if it exists (we'll recreate it later)
    if 'idx' in df.columns:
        df.drop('idx', axis=1, inplace=True)
    
    df.set_index('date', inplace=True)

    daily_df = df.resample('1D').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'
    })

    daily_df.dropna(inplace=True)
    daily_df.reset_index(inplace=True)
    
    # Add idx column based on the new index
    daily_df['idx'] = daily_df.index
    
    print("Daily resampling completed successfully.")
    return daily_df

def resample_to_weekly(df):
   
    if 'date' not in df.columns:
        raise ValueError("Expected 'date' column in DataFrame.")
    
    print("Resampling data to weekly frequency...")
    # Make a copy to avoid SettingWithCopyWarning
    df = df.copy()
    
    # Drop idx if it exists (we'll recreate it later)
    if 'idx' in df.columns:
        df.drop('idx', axis=1, inplace=True)
    
    df.set_index('date', inplace=True)

    weekly_df = df.resample('1W').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'
    })

    weekly_df.dropna(inplace=True)
    weekly_df.reset_index(inplace=True)
    
    # Add idx column based on the new index
    weekly_df['idx'] = weekly_df.index
    
    print("Weekly resampling completed successfully.")
    return weekly_df

def resample_to_hourly(df):
   
    if 'date' not in df.columns:
        raise ValueError("Expected 'date' column in DataFrame.")
    
    print("Resampling data to hourly frequency...")
    # Make a copy to avoid SettingWithCopyWarning
    df = df.copy()
    
    # Drop idx if it exists (we'll recreate it later)
    if 'idx' in df.columns:
        df.drop('idx', axis=1, inplace=True)
    
    df.set_index('date', inplace=True)

    hourly_df = df.resample('1h').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'
    })

    hourly_df.dropna(inplace=True)
    hourly_df.reset_index(inplace=True)
    
    # Add idx column based on the new index
    hourly_df['idx'] = hourly_df.index
    
    print("Hourly resampling completed successfully.")
    return hourly_df


