import finplot as fplt
import MetaTrader5 as mt5
import pandas as pd

mt5.initialize()

rates = mt5.copy_rates_from_pos('USDTRY', mt5.TIMEFRAME_D1, 100, 90)

rates_frame = pd.DataFrame(rates)

rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

# candles = rates_frame[['time', 'open', 'high', 'low', 'close']]
# fplt.candlestick_ochl(candles)

fplt.show()