import itertools
import pandas as pd
from tqdm import tqdm  # Optional: for progress bar

def get_top_correlated_trios(stock_data_manager, stock_list, month, year, top_n=50):
    """
    Finds top N positively and negatively correlated trios of stocks.
    
    Args:
        stock_data_manager (StockDataManager): Your data manager instance
        stock_list (list): List of stock symbols
        month (int): Month number
        year (int): Year
        top_n (int): Number of top correlated trios to return

    Returns:
        Tuple of lists:
            - Top N positively correlated trios (sorted descending)
            - Top N negatively correlated trios (sorted ascending)
    """
    trio_scores = []

    for trio in tqdm(itertools.combinations(stock_list, 3), desc="Evaluating trios"):
        try:
            dfs = []
            for symbol in trio:
                df = stock_data_manager.get_data_for_month(symbol, month, year)
                df = df.set_index("date")[["return_token"]].rename(columns={"return_token": symbol})
                dfs.append(df)

            combined_df = pd.concat(dfs, axis=1)
            combined_df.dropna(inplace=True)

            if combined_df.shape[0] < 5:
                continue  # Not enough data points

            corr_matrix = combined_df.corr()
            avg_corr = (corr_matrix.iloc[0,1] + corr_matrix.iloc[0,2] + corr_matrix.iloc[1,2]) / 3
            trio_scores.append((trio, avg_corr))

        except Exception as e:
            continue  # Ignore combos that cause errors

    # Sort trios
    sorted_by_corr = sorted(trio_scores, key=lambda x: x[1])
    top_negative = sorted_by_corr[:top_n]
    top_positive = sorted_by_corr[-top_n:][::-1]  # highest first

    return top_positive, top_negative
