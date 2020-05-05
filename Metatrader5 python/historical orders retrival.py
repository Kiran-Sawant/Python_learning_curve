import MetaTrader5 as mt5
import datetime as dt

mt5.initialize()

#____________retriving no of historical trades___________#
fromDate = dt.datetime(2019, 8, 1)
toDate = dt.datetime.now()
historyOrder = mt5.history_orders_total(fromDate, toDate)  #retrives number of trades in time range
print("Total history orders:", historyOrder)

#_________retriving historical order information__________#
orerData = mt5.history_orders_get(fromDate, toDate) #by date range
for i in orerData:
    print(i)

orderData2 = mt5.history_orders_get(ticket=38110138) #by tickets
for data in orderData2:
    print('\n', data)

#______total no of historical deals(executed orders)_______#
deals = mt5.history_deals_total(fromDate, toDate)
print("\nTotal deals:", deals)


#__________get information of historical deals___________#
deals = mt5.history_deals_get(fromDate, toDate) #by date range
for i in deals:
    print(i)

deal = mt5.history_deals_get(ticket=17371248)   #by tickets
print(deal[0], '\n')
for i in deal[0]:
    print(i)

mt5.shutdown()