import xlwings as xl
import pandas as pd
import numpy as np

wBook = xl.Book('experiment.xlsx')
data = wBook.sheets('data')

#________________dictionary converter______________#
#reading
k = data.range('A2:B12').options(dict).value #converts data from two coloumns into python dictionary
print(k)                                     #where values in 1st coloumn are keys & in 2nd are dict values
#writing
#data.range('A2:B12').options(dict).value = dict() #does the inverse of line 10

#________________Numpy array converter________________#
#reading
j = data.range('B2:B12').options(np.array, transpose=True).value #puts the values in given the range into a numpy array
print(j)
#writing
data.range('E2:E12').options(transpose=True).value = np.array([1,2,3,4,5,6,7,8,9,10,11]) #inserts the given np array into the range

#_______________Pandas Series Converter_______________#
#reading
panda = data.range('A1',).options(pd.Series, expand='table', header=True).value
print('\n', panda)
#writing
data.range('A17').options(header=True).value = panda

#_______________Pandas DataFrame converter_____________#
#reading
frame = data.range('A1:C12').options(pd.DataFrame, header=1).value
print('\n', frame)
#writing
data.range('E17').value = frame