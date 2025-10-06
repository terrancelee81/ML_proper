# services/data_fetcher.py
import yfinance as yf

class DataFetcher:
    def __init__(self, ticker):
        self.ticker = ticker

    def fetch(self, start="2020-01-01", end="2023-01-01"):
        data = yf.download(self.ticker, start=start, end=end)
        return data