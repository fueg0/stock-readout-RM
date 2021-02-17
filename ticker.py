import yfinance as yf

# define the ticker symbol
tickerSymbol = []


def get_stocks(ticker):
    ask_stock = str(input("What is the ticker of the stock you'd like data for?\n"))
    tickerSymbol.append(ask_stock)
    add_more = ask_more()

    while add_more == "y":
        ask_stock = str(input("What is the ticker of the stock you'd like data for?\n"))
        tickerSymbol.append(ask_stock)
        add_more = input("Would you like to add another? (y/n)\n")

    for item in tickerSymbol:
        current_lastClose_open(item)


def ask_more():
    add_more = input("Would you like to add another? (y/n)\n")
    return add_more


def current_lastClose_open(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1m')

    current_price = "Current Price: " + str(todays_data['Close'][0])
    open = "Open Price: " + str(ticker.info["regularMarketOpen"])
    close = "Last Closing Price: " + \
            str(ticker.info["regularMarketPreviousClose"])
    data = [symbol, open, close, current_price]
    return print_stocks(data)


def current_price():
    symbol = str(input("What ticker do you want to see?\n"))
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1m')

    current_price = "Current Price: " + str(todays_data['Close'][0])
    return print(current_price)


def print_stocks(stock):
    for item in stock:
        print(item)
    print("\n")


get_stocks(tickerSymbol)