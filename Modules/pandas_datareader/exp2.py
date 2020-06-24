import pandas_datareader.data as web
# from pandas_datareader.yahoo import options
import datetime as dt
# import matplotlib.pyplot as plt
import pandas as pd
import finplot as fin

assets = {'Alphabet': 'GOOGL',
        'Verizon': 'VZ',
        'Amazon': 'AMZN',
        'Coca-cola': 'KO',
        'JP-Morgan': 'JPM',
        'General Electric': 'GE',
        'Goldman': 'GS'}

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

fb = web.DataReader(assets['Goldman'], 'yahoo', start, end)
# print(fb)
candles = fb[['Open', 'Close', 'High', 'Low']]
fin.create_plot(title='Goldman')
fin.candlestick_ochl(candles)

fin.show()
