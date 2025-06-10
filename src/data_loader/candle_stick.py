import matplotlib.pyplot as plt

def pltCandleStick(data, figsize=(14, 6)):
    
    candle_data = generateCandleStick(data)
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


def generateCandleStick(df):
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

