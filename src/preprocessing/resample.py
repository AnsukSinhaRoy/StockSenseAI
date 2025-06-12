
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

