import MetaTrader5 as mt5
import datetime as dt
import pytz

#____________Initializing Metatrader5____________#
mt5.initialize()
print(f"Module Author: {mt5.__author__}")
print(f"MetaTrader5 module version: {mt5.__version__}")
print(f"MT5 Terminal Build: {mt5.terminal_info().build}")


#__________Pending Order operations_____________#
no_of_orders = mt5.orders_total()#changed                        #returns total number of pending orders
print('no of pending orders: {0}'.format(no_of_orders))

order = mt5.orders_get()                                         #returns information of passed pending order, returns all if nothing passed
print('\nOrder info: {0}'.format(order))

#_______Making and viewing an orders dictionary_______#
if order == None:
    print(f"No Orders, error code={mt5.last_error()}")
else:
    for i in range(len(order)):
        k = order[i]._asdict()                                   #._asdict() works with named tuple and not a tuple.
        print('\n')
        for j in k:
            print(f"{j}: {k[j]}")


#____________Calculating required Margin_________________#
margin = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, order[0].symbol, order[0].volume_initial, order[0].price_open) #returns required margin in account currency
print('\nMargin requirement for buying {0} @ {1} is ${2}'.format(order[0].symbol, order[0].price_open, margin))


#____________Calculating Profit/loss_____________#
volatility = float(input('Enter the desired volatility in percentage: '))
percentage = volatility * (order[0].price_open / 100)
profit = mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, order[0].symbol, order[0].volume_initial, order[0].price_open, (order[0].price_open + percentage)) #returns potential P/L in account currency
print('\n Profit on {0} at {1} with {2}% volatility is ${3}'.format(order[0].symbol, order[0].price_open, volatility, profit))


#________Open positions________#
openPos = mt5.positions_total()             #returns total number of open positions
print('\nno of open positions:', openPos)

position = mt5.positions_get()
"""Returns info of open positions as a named tuple
one can pass name of the asset to show all open psitions on that asset
one can pass a ticket of a trade to see the status of that trade
If nothing is passed, it returns info of all the open positions in MT5"""

#________Printing all the values of a position as a dictionary___________#
if position == None:
    print(f"No positions, error code={mt5.last_error()}")
else:
    for i in range(len(position)):
        k = position[i]._asdict()               #._asdict() works with named tuple and not a tuple.
        print('\n')                             #for a tuple of named tuple apply it on single elements of the tuple.
        for j in k:
            print(f"{j}: {k[j]}")