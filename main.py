from datetime import datetime
from math import pow

class Stock:
    def __init__(self, symbol, prices):
        self.symbol = symbol
        self.prices = prices

    def price(self, date):
        return self.prices.get(date)

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock, quantity):
        self.stocks[stock.symbol] = {'stock': stock, 'quantity': quantity}

    def profit(self, start_date, end_date):
        start_value = 0
        end_value = 0

        for stock_info in self.stocks.values():
            stock = stock_info['stock']
            quantity = stock_info['quantity']

            start_price = stock.price(start_date)
            end_price = stock.price(end_date)
          
            if start_price is None or end_price is None:
                continue

            start_value += start_price * quantity
            end_value += end_price * quantity

        return end_value - start_value

    def annualized_return(self, start_date, end_date):
        initial_profit = self.profit(start_date, end_date)

        start_value = sum(stock_info['stock'].price(start_date) * stock_info['quantity']
                          for stock_info in self.stocks.values()
                          if stock_info['stock'].price(start_date) is not None)

        if start_value == 0:
            return None


        days = (end_date - start_date).days
        years = days / 365.25

        return pow((initial_profit / start_value) + 1, 1 / years) - 1
