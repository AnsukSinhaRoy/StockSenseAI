import pandas as pd

def heikin_ashi(df):
    print("Calculating Heikin-Ashi values...")
    
    # Verify required columns are present
    required_cols = ['open', 'high', 'low', 'close']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"DataFrame must contain these columns: {required_cols}")
    
    ha_df = df.copy()
    
    # Calculate Heikin-Ashi values
    ha_df['close'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4
    
    # Initialize first HA open
    if len(ha_df) > 0:
        ha_df.loc[ha_df.index[0], 'open'] = (df.loc[df.index[0], 'open'] + df.loc[df.index[0], 'close']) / 2
    
    # Calculate subsequent HA opens
    for i in range(1, len(ha_df)):
        ha_df.loc[ha_df.index[i], 'open'] = (ha_df.loc[ha_df.index[i-1], 'open'] + ha_df.loc[ha_df.index[i-1], 'close']) / 2
    
    # Calculate HA high and low
    ha_df['high'] = ha_df[['open', 'close', 'high']].max(axis=1)
    ha_df['low'] = ha_df[['open', 'close', 'low']].min(axis=1)
    
    # Keep original volume (Heikin-Ashi typically doesn't modify volume)
    if 'volume' in df.columns:
        ha_df['volume'] = df['volume']
    
    return ha_df