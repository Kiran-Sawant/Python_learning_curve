"""plotting OCHLV, EMAs & stddev"""

import MetaTrader5 as mt5
import finplot as fplt
import pandas as pd

mt5.initialize()


# symbol = input('Enter the symbol').upper()

rates = pd.DataFrame(mt5.copy_rates_from_pos('EURUSD', mt5.TIMEFRAME_H1, 1, 240)).drop(columns=['spread', 'real_volume'])
rates['time'] = pd.to_datetime(rates['time'], unit='s')

#______Plotting_______#
ax, ax2 = fplt.create_plot(title='EURUSD H1', rows=2)
axo = ax.overlay()

fplt.candlestick_ochl(rates[['time', 'open', 'close', 'high', 'low']], ax=ax)
fplt.volume_ocv(rates[['time', 'open', 'close', 'tick_volume']], ax=axo)

fplt.plot(rates['close'].ewm(8).mean(), legend='8 EMA', ax=ax)
fplt.plot(rates['close'].ewm(24).mean(), legend='24 EMA', ax=ax)

roll_std = (rates['close'].rolling(24).std()) * 100
fplt.plot(roll_std, legend='24 std-dev', ax=ax2)
fplt.add_text(ax=ax2, pos=(rates['time'].iloc[-1], roll_std[roll_std.index[-1]]), s=str(roll_std[roll_std.index[-1]]))

# print(roll_std[roll_std.index[-1]])

fplt.show()
mt5.shutdown()