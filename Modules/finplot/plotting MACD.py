import MetaTrader5 as mt5
import finplot as fplt
import pandas as pd
import datetime as dt

mt5.initialize()

#________Setting up Data_________#
symbol = input('Enter symbol: ').upper()

rate = pd.DataFrame(mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H1, 0, 200))

# rate['time'] = pd.to_datetime(rate['time'], unit='s')
# print(rate)

#________Settingup plot________#

# creating multiple windows
ax, ax2 = fplt.create_plot(title=symbol, rows=2)
fplt.candlestick_ochl(rate[['time', 'open', 'close', 'high', 'low']], ax=ax)

# creating volume overlay on 1st window
axo = ax.overlay()
fplt.volume_ocv(rate[['time', 'open', 'close', 'tick_volume']], ax=axo)

#_________plotting MACD on 2nd window__________#
# MACD line
macd = rate['close'].ewm(span=12).mean() - rate['close'].ewm(span=26).mean()

#signal line
signal = macd.ewm(span=9).mean()

rate['macd_diff'] = macd - signal

# plotting MACD histogram
fplt.volume_ocv(rate[['time', 'open', 'close', 'macd_diff']], ax= ax2)
# plotting MACD line
fplt.plot(macd, ax=ax2, legend='MACD')
# plotting signal line
fplt.plot(signal, ax=ax2, legend='Signal')

fplt.show()
mt5.shutdown()