ticker = 'NTPC'

url1 = f'https://www.google.com/finance/quote/{ticker}:NSE'

import requests
from bs4 import BeautifulSoup
import time

def fetch_current_price(ticker):
    url = f'https://www.google.com/finance/quote/{ticker}:NSE'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    Priceclass = "YMlKec fxKbKc"    
    price = soup.find(class_=Priceclass).text.strip()[1:].replace(',', '')
    return float(price)



def fetch_news_links_google_finance(ticker, days=7):
    """
    Fetches news headlines and real article URLs from Google Finance news section for a given NSE stock ticker.

    Args:
        ticker (str): Stock ticker symbol (e.g., "NTPC").
        days (int): Not used here (Google Finance doesn't expose dates via URL), but kept for compatibility.

    Returns:
        List of tuples: Each tuple is (headline, article_url)
    """
    url = f'https://www.google.com/finance/quote/{ticker}:NSE'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_class = "yY3Lee"
    news_blocks = soup.find_all("div", class_=news_class)
    news_items = []

    for block in news_blocks:
        try:
            # Find <a> tag with href inside
            a_tag = block.find("a", href=True)
            headline_div = block.find("div", class_="Yfwt5")
            if a_tag and headline_div:
                article_url = a_tag['href']
                headline = headline_div.text.strip()
                news_items.append((headline, article_url))
        except Exception as e:
            print(f"Error parsing news block: {e}")
            continue

    return news_items


print(fetch_current_price(ticker))
news = fetch_news_links_google_finance(ticker)
for title, link in news:
    print(f"📰 {title}\n🔗 {link}\n")

