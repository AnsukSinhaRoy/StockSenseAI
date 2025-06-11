import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compute_return_token(df, bins=[-0.04, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04]):
    """
    Create discrete tokens based on % return in ha_close.
    """
    df = df.copy()
    df['pct_change'] = df['close'].pct_change().fillna(0)
    df['return_token'] = pd.cut(df['pct_change'], 
                                bins=[-np.inf] + bins + [np.inf],
                                labels=False)
    return df

def compute_pct_change(df, bins=[-0.04, -0.03, -0.02, -0.01, 0, 0.01, 0.02, 0.03, 0.04]):
    """
    Create discrete tokens based on % return in ha_close.
    """
    df = df.copy()
    df['pct_change'] = df['close'].pct_change().fillna(0)
    return df

def compute_shape_ratio(df):
    """
    Compute candle shape ratio (ha_close - ha_open) / (ha_high - ha_low)
    """
    df = df.copy()
    candle_range = df['high'] - df['low']
    candle_range[candle_range == 0] = 1e-6  # prevent divide by zero
    df['shape_ratio'] = (df['close'] - df['open']) / candle_range
    return df

def compute_volume_spike(df, window=10):
    """
    Compute volume spike as ratio to rolling mean.
    """
    df = df.copy()
    df['volume_mean'] = df['volume'].rolling(window=window).mean()
    df['volume_spike'] = df['volume'] / df['volume_mean']
    df['volume_spike'] = df['volume_spike'].fillna(1)
    return df

def hybrid_tokenize(df, volume_window=10):
    """
    Combine all features into a single encoded DataFrame.
    """
    df = compute_return_token(df)
    df = compute_shape_ratio(df)
    df = compute_volume_spike(df, window=volume_window)

    # Drop intermediate columns
    df = df.drop(columns=['pct_change', 'volume_mean'])

    return df



def plot_return_token_distribution(df):
    """
    Plot histogram of return_token frequency.
    """
    token_counts = df['return_token'].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    plt.bar(token_counts.index.astype(str), token_counts.values, color='skyblue')
    plt.title("Distribution of Return Tokens")
    plt.xlabel("Return Token Index")
    plt.ylabel("Frequency")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()
