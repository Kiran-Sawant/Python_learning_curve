import MetaTrader5 as mt5
import datetime as dt
import pytz

#____________Initializing Metatrader5____________#
mt5.initialize()
print(mt5.version(), '\n')
print(mt5.terminal_info(), '\n')
print(mt5.account_info(), '\n')


#__________Pending Order operations_____________#
orders = mt5.orders_total()#changed                        #returns total number of pending orders
print('no of pending orders: {0}'.format(orders))

order = mt5.orders_get()                            #returns information of passed pending order, returns all if nothing passed
print('\nOrder info: {0}'.format(order))


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

for i in position:
    print('\n', i)