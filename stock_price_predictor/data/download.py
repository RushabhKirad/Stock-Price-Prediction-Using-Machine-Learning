import yfinance as yf
import pandas as pd

def download_stock_data(ticker="AAPL", start="2018-01-01", end="2025-07-09"):
    df = yf.download(ticker, start=start, end=end)
    df.to_csv(f"data/{ticker}_stock_data.csv")
    print(f"Data saved to data/{ticker}_stock_data.csv")
    return df

# Example usage
if __name__ == "__main__":
    df = download_stock_data("TCS.NS")
    print(df.head())

# This code downloads stock data for a given ticker and saves it to a CSV file.
# It uses the yfinance library to fetch the data and pandas to handle the DataFrame.