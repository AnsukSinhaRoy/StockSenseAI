import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta
import pytz

# Define Indian timezone
IST = pytz.timezone('Asia/Kolkata')

def fetch_current_price(ticker):
    """
    Fetches the current market price of a given NSE ticker from Google Finance.
    """
    try:
        url = f'https://www.google.com/finance/quote/{ticker}:NSE'
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        price_tag = soup.find("div", class_="YMlKec fxKbKc")
        if not price_tag:
            raise ValueError("Price not found")

        price_str = price_tag.text.strip().replace(',', '').replace('₹', '')
        return float(price_str)
    except Exception as e:
        print(f"❌ {ticker}: {e}")
        return None

def is_market_open():
    """
    Returns True if current time is within NSE trading hours (Mon–Fri, 9:15–15:30 IST).
    """
    now = datetime.now(IST)
    if now.weekday() >= 5:
        return False  # Weekend
    open_time = now.replace(hour=9, minute=15, second=0, microsecond=0)
    close_time = now.replace(hour=15, minute=30, second=0, microsecond=0)
    return open_time <= now <= close_time

def fetch_prices_batch(tickers):
    """
    Fetch prices for a list of tickers.
    """
    prices = {}
    for symbol in tickers:
        price = fetch_current_price(symbol)
        prices[symbol] = price if price is not None else "N/A"
        time.sleep(1.2)  # throttle per request
    return prices

def run_live_fetch(tickers):
    print("🟢 Live price fetcher started. Press Ctrl+C to stop.")
    try:
        while True:
            if is_market_open():
                print(f"\n⏰ {datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')} IST - Fetching prices...")
                prices = fetch_prices_batch(tickers)
                for ticker, price in prices.items():
                    print(f"🔹 {ticker}: ₹{price}")
            else:
                print(f"\n⏳ Market is closed. Next check in 1 minute... [{datetime.now(IST).strftime('%H:%M:%S')}]")

            time.sleep(60)
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user.")

# === Use it like this ===
tickers = ['NTPC', 'RELIANCE', 'TCS', 'INFY']
run_live_fetch(tickers)
