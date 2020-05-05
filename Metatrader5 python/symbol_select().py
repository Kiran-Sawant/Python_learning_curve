import  MetaTrader5 as mt5
import time

mt5.initialize()

aset_list = ['EURUSD', 'USDZAR', 'EURNOK', 'EURCHF']

def insertion(symbol):
    mt5.symbol_select(symbol, True)


for asset in aset_list:
    tick = mt5.symbol_info_tick(asset)
    if tick == None:
        insertion(asset)
        time.sleep(5)
        tick = mt5.symbol_info_tick(asset)
    print(tick)