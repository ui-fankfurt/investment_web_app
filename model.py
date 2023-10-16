import pandas as pd
import yfinance as yf
import datetime as dt
import talib as ta
import matplotlib.pyplot as plt



end = dt.datetime.now()
start = end - dt.timedelta(days = 500)


def plotting(ticker):
    data = yf.download(ticker, start, end)

    data['SMA_100'] = ta.SMA(data["Close"], 100)
    data['SMA_200'] = ta.SMA(data["Close"], 200)
    data['SMA_500'] = ta.SMA(data["Close"], 500)

    data["SMA_10"] = ta.SMA(data["Close"], 10)
    data["SMA_20"] = ta.SMA(data["Close"], 20)
    data["SMA_50"] = ta.SMA(data["Close"], 50)

    data["RSI"] = ta.RSI(data["Close"])

    macd, macd_signal, macd_hist = ta.MACD(data["Close"])

    fig, axs = plt.subplots(3,1, gridspec_kw = {"height_ratios": [4,1,2]}, figsize = (15,10))
    c = ['red' if c1 <0 else 'green' for c1 in macd_hist]

    axs[0].plot(data["Close"])
    axs[0].plot(data["SMA_10"])
    axs[0].plot(data["SMA_20"])
    axs[0].plot(data["SMA_50"])
    axs[1].axhline(y=70, color = "r", linestyle = "--")
    axs[1].axhline(y=30, color = "g", linestyle = "--")
    axs[1].plot(data["RSI"], color = "orange")
    axs[2].plot(macd, 'b-')
    axs[2].plot(macd_signal, '--', color = "orange")
    axs[2].bar(macd_hist.index, macd_hist, color = c)

    plt.savefig(f"static/graph.png")



