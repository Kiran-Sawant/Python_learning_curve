import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt

fred = {'Real GDP': 'A191RL1Q225SBEA',
        'M2': 'M2',
        'fedfundsrate': 'FEDFUNDS'}

real_gdp = pdr.DataReader(fred['Real GDP'], 'fred')
interest = pdr.DataReader(fred['fedfundsrate'], 'fred')

real_gdp.plot(kind='line', title='US Real GDP')
interest.plot(kind='line', title='Effective Fed Funds rate')

plt.show()

# print(interest)