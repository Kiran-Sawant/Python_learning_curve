import MetaTrader5 as mt5
import datetime as dt
import pytz

#____________Initializing Metatrader5____________#
mt5.initialize()
print(mt5.version(), '\n')
print(mt5.terminal_info(), '\n')
print(mt5.account_info(), '\n')

timezone = pytz.timezone('UTC')
tiem = dt.datetime(2020, 2, 28)
tiem2 = dt.datetime(2020, 2, 29)


#____________Symbol info____________#
# mt5.symbol_select('EURTRY', False) #puts/removes the entered symbol in the marketwatch

eurinfo = mt5.symbol_info('EURUSD')         #gives the information of the asset
print(eurinfo)
print('='*90, '\n')

eurtick = mt5.symbol_info_tick('EURUSD')    #gives the latest tick info
print('tick info:', eurtick)
print('='*90, '\n')


#_______________retriving OHLC data______________#
eurbar = mt5.copy_rates_from('EURUSD', mt5.TIMEFRAME_H1, tiem, 1)
print('bars: ', eurbar, '\n')
# for i in eurbar:
#     print(i)

eurbar2 = mt5.copy_rates_range('EURUSD', mt5.TIMEFRAME_H1, tiem, tiem2)
print('bars range: ', eurbar2, '\n')

eurbar3 = mt5.copy_rates_from_pos('EURUSD', mt5.TIMEFRAME_H1, 0, 3)
print('bars from pos:', eurbar3, '\n')
print('='*90, '\n')


#__________________retriving ticks____________________#
eurtic = mt5.copy_ticks_from('EURUSD', tiem, 3, mt5.COPY_TICKS_INFO)
print('EURUSD Tic', eurtic, '\n')

eurtic2 = mt5.copy_ticks_range('EURUSD', tiem, tiem2, mt5.TIMEFRAME_H1)
print('EURUSD Tic range',eurtic2, '\n')