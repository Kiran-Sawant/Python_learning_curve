import MetaTrader5 as mt5


#____________Initializing Metatrader5____________#
mt5.initialize()
print(mt5.version(), '\n')
print(mt5.terminal_info(), '\n')
print(mt5.account_info(), '\n')

order = mt5.orders_get()        #getting all pending orders

#____________Calculating required Margin_________________#
margin = mt5.order_calc_margin(mt5.ORDER_TYPE_BUY, order[0].symbol, order[0].volume_initial, order[0].price_open) #returns required margin in account currency
print('\nMargin requirement for buying {0} @ {1} is ${2}'.format(order[0].symbol, order[0].price_open, margin))


#____________Calculating Profit/loss_____________#
volatility = float(input('Enter the desired volatility in percentage: '))
percentage = volatility * (order[0].price_open / 100)
profit = mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, order[0].symbol, order[0].volume_initial, order[0].price_open, (order[0].price_open + percentage)) #returns potential P/L in account currency
print('\n Profit on {0} at {1} with {2}% volatility is ${3}'.format(order[0].symbol, order[0].price_open, volatility, profit))