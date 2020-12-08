"""     .symbol_select(s) takes a symbol as string and a boolean
    and adds the symbol in the market watch if boolean is True
    and removes the symbol from the market watch if boolean set
    to False.
        While retriving price data from selected symbol, pause the
    program for a few seconds as it takes time to download price
    data due to network lag"""

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
        time.sleep(5)               # pausing program
        tick = mt5.symbol_info_tick(asset)
    print(tick)