import MetaTrader5 as mt5
import pandas as pd

mt5.initialize()                    #Connecting the program to MT5
print(mt5.version(), '\n')          #Version info of MT5 software

#___________Creating a terminal info dictionary____________#
trm_dict = mt5.terminal_info()._asdict()        #status info of the MT5 terminal
for i in trm_dict:
    print("{0}: {1}".format(i, trm_dict[i]))

#____________Creating an account info dictionary____________#
account_dict = mt5.account_info()._asdict()     #various information of the loggedin account
for i in account_dict:
    print(i, ':', account_dict[i])

#_______________puttng info in a pandas DataFrame_______________#
account_df = pd.DataFrame(list(account_dict.items()), columns=['property', 'value'])
trm_df = pd.DataFrame(list(trm_dict.items()), columns=['property', 'value'])

#_________________Brokerage account Login example_________________________#
'''SYNTAX: mt5.login(loginID, server='server_name', password='p@$$W0rd')'''

loginID = 14000510
authentication = mt5.login(loginID, server='MetaQuotes-Demo', password='qvpzit7t')

if authentication:
    print(mt5.account_info())
else:
    print("failed to login to trade account {0}".format(loginID))


print(mt5.last_error())             #Returns error if any
mt5.shutdown()                      #break connection with MT5 Terminal