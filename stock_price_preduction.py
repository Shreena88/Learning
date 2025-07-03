import requests
import matplotlib.pyplot as plt

API_KEY = '4WP8XPF8EQ8RZ00F'
BASE_URL = 'https://www.alphavantage.co/support/query'

#Fetches the stock data
def fetch_stock_data(symbol):
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

#Extracts dates and price from the input symbol
def parse_data(data):
    time_series = data.get('Time Series (Daily)',{})
    dates = []
    prices = []
    for date,stats in time_series.items():
        dates.append(date)
        prices.append(float(stats.get('4. close')))
    return dates, prices

#Provide visualization of stock price
def plot_data(dates, prices,symbol):
    plt.figure(figsize=(10,5))
    plt.plot(dates, prices, label=f'{symbol} Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price(USD)')
    plt.title(f'{symbol} Stock Price Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

def main():
    symbol = input("Enter stock ticker symbol: ").upper()
    data = fetch_stock_data(symbol)
    if 'Time Series (Daily)' in data:
        dates, prices = parse_data(data)
        plot_data(dates, prices, symbol)
    else:
        print(f"Error: Unable to fetch data from {symbol}")

if __name__ == '__main__':
    main()
