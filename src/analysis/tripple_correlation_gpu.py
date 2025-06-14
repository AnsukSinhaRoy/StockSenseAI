import itertools
import numpy as np
import cupy as cp
import pandas as pd
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')

def get_top_correlated_trios_gpu(stock_data_manager, stock_list, month, year, top_n=10, verbose=False):
    """
    GPU-accelerated correlation using CuPy (no cuDF), works on Windows.

    Args:
        stock_data_manager: Instance of StockDataManager.
        stock_list (list): List of stock symbols.
        month (int): Month number.
        year (int): Year.
        top_n (int): Number of top positive/negative correlations.
        verbose (bool): If True, prints/logs detailed status.

    Returns:
        Tuple: (top_positive, top_negative)
    """
    trio_scores = []

    combos = list(itertools.combinations(stock_list, 3))
    pbar = tqdm(combos, desc="Evaluating Trios on GPU", ncols=100)

    for trio in pbar:
        try:
            if verbose:
                logging.info(f"Processing trio: {trio}")

            dfs = []
            for symbol in trio:
                df = stock_data_manager.get_data_for_month(symbol, month, year)
                if df.empty:
                    raise ValueError(f"No data for {symbol} in {month}/{year}")
                df = df.set_index("date")[["return_token"]].rename(columns={"return_token": symbol})
                dfs.append(df)

            combined_df = pd.concat(dfs, axis=1).dropna()

            if combined_df.shape[0] < 5:
                if verbose:
                    logging.info(f"Skipping {trio} due to insufficient data")
                continue

            # Convert to CuPy array
            gpu_array = cp.asarray(combined_df.values)

            # Compute correlation on GPU
            corr_matrix = cp.corrcoef(gpu_array.T)

            # Average of 3 pairwise correlations
            avg_corr = (corr_matrix[0, 1] + corr_matrix[0, 2] + corr_matrix[1, 2]) / 3
            avg_corr = float(avg_corr.get())  # Convert back to Python float

            trio_scores.append((trio, avg_corr))
            pbar.set_postfix_str(f"Last Corr: {avg_corr:.3f}")

        except Exception as e:
            if verbose:
                logging.warning(f"Skipping trio {trio}: {e}")
            continue

    # Sort results
    sorted_by_corr = sorted(trio_scores, key=lambda x: x[1])
    top_negative = sorted_by_corr[:top_n]
    top_positive = sorted_by_corr[-top_n:][::-1]

    return top_positive, top_negative
