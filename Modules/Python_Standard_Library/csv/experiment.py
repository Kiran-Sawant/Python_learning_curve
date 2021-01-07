"""This experiment takes a csv and converts it into a pandas dataframe
    and then plots it."""

import csv
import pandas as pd
import matplotlib.pyplot as plt

with open('XBRXTI_Daily_jan~may-2020.csv', mode='r') as xbrxti:
    # infos = csv.reader(xbrxti, delimiter='\t')
    infos = csv.DictReader(xbrxti, delimiter='\t')

    # Converting an ordered dictionary to a list
    infolist = list((info['<DATE>'], float(info['<OPEN>']), float(info['<HIGH>']), float(info['<LOW>']), float(info['<CLOSE>'])) for info in infos)

    # Making dataframe
    df = pd.DataFrame(infolist, columns=['date', 'open', 'high', 'low', 'close'])

    # ploting the dataframe
    df.plot(kind='line', x='date', y=['open', 'high', 'low', 'close'], title='Brent vs WTI')

    # displaying the plot
    plt.show()