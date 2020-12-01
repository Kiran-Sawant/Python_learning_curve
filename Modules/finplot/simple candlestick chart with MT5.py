import finplot as fplt
import MetaTrader5 as mt5
import pandas as pd
# import pandas_datareader as pdr
import datetime as dt

# starting MT5
mt5.initialize()

# setting dates
# t1 = dt.datetime.now()
# t2 = t1 - dt.timedelta(days=20)

# extracting 'EURUSD' daily rates from MT5.
rate = mt5.copy_rates_from_pos('USDRUB', mt5.TIMEFRAME_D1, 0, 20)

# converting the extracted tuple to DataFrame.
ratedf = pd.DataFrame(rate)
# print(ratedf)

# converting UNIX timestamps in 'time' column to datetime.
ratedf['time'] = pd.to_datetime(ratedf['time'], unit='s')

# ploting candlestick graph.
fplt.candlestick_ochl(ratedf[['time', 'open', 'close', 'high', 'low']])

# plotting line graph of daily open price.
# fplt.plot(ratedf.index, ratedf['open'], legend='Open')

fplt.show()
mt5.shutdown()
