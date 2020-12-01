"""A PandasDataSource object can be created to pass as argument in
candlestick_ochl() function."""

import pandas_datareader as pdr
import finplot as fplt

# Getting timeseries
k = pdr.DataReader('AAPL', data_source='yahoo', start='2020-01-01')

# Setting PandasDataSource objects for OCHL & volume
price = fplt.PandasDataSource(k[['Open', 'Adj Close', 'High', 'Low']])
volume = fplt.PandasDataSource(k[['Open', 'Close', 'Volume']])

# Setting Graph window with 2 axes
ax, ax2 = fplt.create_plot(title='Aaple Inc', rows=2)
# Setting overlay on first axis
axo = ax.overlay()

# plotting candlestick chart
fplt.candlestick_ochl(price)

# fplt.volume_ocv(volume, ax=axo)       # plotting volume on overlay.
fplt.volume_ocv(volume, ax=ax2)         # plotting volume on second axis.

# Adding text on top left corner
fplt.add_text(ax=ax, pos=(k.index[1], k.High[-1]), s='Aaple Inc')


fplt.show()