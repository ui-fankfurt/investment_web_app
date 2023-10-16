from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG
import talib as ta
import pandas_datareader as web
import datetime as dt
import yfinance as yf

class MyMACDStrategy(Strategy):

    def init(self):
        price = self.data.Close
        self.macd = self.I(lambda x: ta.MACD(x)[0], price)
        self.macd_signal = self.I(lambda x: ta.MACD(x)[1], price)

    def next(self):
        if crossover(self.macd, self.macd_signal):
            self.buy()
        elif crossover(self.macd_signal, self.macd):
            self.sell()


start =  dt.datetime(2021, 1,1)
end = dt.datetime.now()
data = yf.download("TSLA", start, end)

backtest = Backtest(data, MyMACDStrategy, commission=.002, exclusive_orders=True)

print(backtest.run())

backtest.plot()
    
        

