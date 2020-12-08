import MetaTrader5 as mt5
import datetime as dt
import pytz

#____________Initializing Metatrader5____________#
mt5.initialize()
print(f"Module Author: {mt5.__author__}")
print(f"MetaTrader5 module version: {mt5.__version__}")
print(f"MT5 Terminal Build: {mt5.terminal_info().build}")


#__________Pending Order operations_____________#
# Returns total number of pending orders as int
no_of_orders = mt5.orders_total()
print('no of pending orders: {0}'.format(no_of_orders))

# Returns information of passed pending order as a tuple of named tuples, returns all orders if nothing passed.
order = mt5.orders_get()
print('\nOrder info: {0}'.format(order))


#_______Making and viewing an ordered dictionary_______#
if order == None:
    print(f"No Orders, error code={mt5.last_error()}")
else:
    for i in range(len(order)):
        # Converting a namedtuple to an ordered dictionary.
        #._asdict() works with named tuple and not a ordinary tuple.
        k = order[i]._asdict()
        print('\n')
        for j in k:
            print(f"{j}: {k[j]}")


#________Open positions________#
openPos = mt5.positions_total()             #returns total number of open positions
print('\nno of open positions:', openPos)

position = mt5.positions_get()
"""Returns info of open positions as a tuple of named tuples
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