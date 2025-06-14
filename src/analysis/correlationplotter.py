
from data.stock_data_manager import StockDataManager
from correlation_plotter import CorrelationPlotter
import pandas as pd
from analysis.tripple_correlation import get_top_correlated_trios
from analysis.tripple_correlation_gpu import get_top_correlated_trios_gpu

stock_files = {
    # Previous entries
    "ABB": "data/raw/ABB_minute.csv",
    "ADANIENSOL": "data/raw/ADANIENSOL_minute.csv",
    "ADANIENT": "data/raw/ADANIENT_minute.csv",
    "ADANIGREEN": "data/raw/ADANIGREEN_minute.csv",
    "ADANIPORTS": "data/raw/ADANIPORTS_minute.csv",
    "ADANIPOWER": "data/raw/ADANIPOWER_minute.csv",
    "AMBUJACEM": "data/raw/AMBUJACEM_minute.csv",
    "APOLLOHOSP": "data/raw/APOLLOHOSP_minute.csv",
    "ASIANPAINT": "data/raw/ASIANPAINT_minute.csv",
    "ATGL": "data/raw/ATGL_minute.csv",
    "AXISBANK": "data/raw/AXISBANK_minute.csv",
    "BAJAJ-AUTO": "data/raw/BAJAJ-AUTO_minute.csv",
    "BAJAJFINSV": "data/raw/BAJAJFINSV_minute.csv",
    "BAJAJHLDNG": "data/raw/BAJAJHLDNG_minute.csv",
    "BAJFINANCE": "data/raw/BAJFINANCE_minute.csv",
    "BANKBARODA": "data/raw/BANKBARODA_minute.csv",
    "BEL": "data/raw/BEL_minute.csv",
    "BHARTIARTL": "data/raw/BHARTIARTL_minute.csv",
    "BHEL": "data/raw/BHEL_minute.csv",
    "BOSCHLTD": "data/raw/BOSCHLTD_minute.csv",
    "BPCL": "data/raw/BPCL_minute.csv",
    "BRITANNIA": "data/raw/BRITANNIA_minute.csv",
    "CANBK": "data/raw/CANBK_minute.csv",
    "CHOLAFIN": "data/raw/CHOLAFIN_minute.csv",
    "CIPLA": "data/raw/CIPLA_minute.csv",
    "COALINDIA": "data/raw/COALINDIA_minute.csv",
    "DABUR": "data/raw/DABUR_minute.csv",
    "DIVISLAB": "data/raw/DIVISLAB_minute.csv",
    "DLF": "data/raw/DLF_minute.csv",
    "DMART": "data/raw/DMART_minute.csv",
    "DRREDDY": "data/raw/DRREDDY_minute.csv",
    "EICHERMOT": "data/raw/EICHERMOT_minute.csv",
    "GAIL": "data/raw/GAIL_minute.csv",
    "GODREJCP": "data/raw/GODREJCP_minute.csv",
    "GRASIM": "data/raw/GRASIM_minute.csv",
    "HAL": "data/raw/HAL_minute.csv",
    "HAVELLS": "data/raw/HAVELLS_minute.csv",
    "HCLTECH": "data/raw/HCLTECH_minute.csv",
    "HDFCBANK": "data/raw/HDFCBANK_minute.csv",
    "HDFCLIFE": "data/raw/HDFCLIFE_minute.csv",
    "HEROMOTOCO": "data/raw/HEROMOTOCO_minute.csv",
    "HINDALCO": "data/raw/HINDALCO_minute.csv",
    "HINDUNILVR": "data/raw/HINDUNILVR_minute.csv",
    "ICICIBANK": "data/raw/ICICIBANK_minute.csv",
    "ICICIGI": "data/raw/ICICIGI_minute.csv",
    "ICICIPRULI": "data/raw/ICICIPRULI_minute.csv",
    "INDIAVIX": "data/raw/INDIA_VIX_minute.csv",
    "INDIGO": "data/raw/INDIGO_minute.csv",
    "INDUSINDBK": "data/raw/INDUSINDBK_minute.csv",
    "INFY": "data/raw/INFY_minute.csv",
    "IOC": "data/raw/IOC_minute.csv",
    "IRCTC": "data/raw/IRCTC_minute.csv",
    "IRFC": "data/raw/IRFC_minute.csv",
    "ITC": "data/raw/ITC_minute.csv",
    "JINDALSTEL": "data/raw/JINDALSTEL_minute.csv",
    "JIOFIN": "data/raw/JIOFIN_minute.csv",
    "JSWENERGY": "data/raw/JSWENERGY_minute.csv",
    "JSWSTEEL": "data/raw/JSWSTEEL_minute.csv",
    "KOTAKBANK": "data/raw/KOTAKBANK_minute.csv",
    "LICI": "data/raw/LICI_minute.csv",
    "LODHA": "data/raw/LODHA_minute.csv",
    "LT": "data/raw/LT_minute.csv",
    "LTIM": "data/raw/LTIM_minute.csv",
    "MARUTI": "data/raw/MARUTI_minute.csv",
    "MOTHERSON": "data/raw/MOTHERSON_minute.csv",
    "NAUKRI": "data/raw/NAUKRI_minute.csv",
    "NESTLEIND": "data/raw/NESTLEIND_minute.csv",
    "NHPC": "data/raw/NHPC_minute.csv",
    "NTPC": "data/raw/NTPC_minute.csv",
    "ONGC": "data/raw/ONGC_minute.csv",
    "PFC": "data/raw/PFC_minute.csv",
    "PIDILITIND": "data/raw/PIDILITIND_minute.csv",
    "PNB": "data/raw/PNB_minute.csv",
    "POWERGRID": "data/raw/POWERGRID_minute.csv",
    "RECLTD": "data/raw/RECLTD_minute.csv",
    "RELIANCE": "data/raw/RELIANCE_minute.csv",
    "SBILIFE": "data/raw/SBILIFE_minute.csv",
    "SBIN": "data/raw/SBIN_minute.csv",
    "SHREECEM": "data/raw/SHREECEM_minute.csv",
    "SHRIRAMFIN": "data/raw/SHRIRAMFIN_minute.csv",
    "SIEMENS": "data/raw/SIEMENS_minute.csv",
    "SUNPHARMA": "data/raw/SUNPHARMA_minute.csv",
    "TATACONSUM": "data/raw/TATACONSUM_minute.csv",
    "TATAMOTORS": "data/raw/TATAMOTORS_minute.csv",
    "TATAPOWER": "data/raw/TATAPOWER_minute.csv",
    "TCS": "data/raw/TCS_minute.csv",
    "TVSMOTOR": "data/raw/TVSMOTOR_minute.csv"
}

#stock_files = {"ABB": "data/raw/ABB_minute.csv","ADANIENSOL": "data/raw/ADANIENSOL_minute.csv","ADANIENT": "data/raw/ADANIENT_minute.csv","ADANIGREEN": "data/raw/ADANIGREEN_minute.csv","ADANIPORTS": "data/raw/ADANIPORTS_minute.csv","ADANIPOWER": "data/raw/ADANIPOWER_minute.csv"}


manager = StockDataManager(stock_files.items())
month = 1
year = 2024

combined_returns = pd.DataFrame()

for symbol in stock_files:
    try:
        df = manager.get_data_for_mo5nth(symbol, month, year)
        df = df.set_index('date')
        combined_returns[symbol] = df['return_token']
    except Exception as e:
        print(f"Skipping {symbol}: {e}")

# Drop any rows with missing values
combined_returns.dropna(inplace=True)

# Plot correlation heatmap
plotter = CorrelationPlotter()
plotter.plot(combined_returns)

# Optional: Display top correlations
CorrelationPlotter.compare_correlations(combined_returns)

# Get top correlated trios
top_positive, top_negative = get_top_correlated_trios(manager, list(combined_returns.columns), month, year)

print("Top 10 Positively Correlated Trios:")
for trio, score in top_positive:
    print(f"{trio} -> Avg Corr: {score:.3f}")

print("\nTop 10 Negatively Correlated Trios:")
for trio, score in top_negative:
    print(f"{trio} -> Avg Corr: {score:.3f}")