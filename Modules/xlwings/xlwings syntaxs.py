import xlwings as xw
import datetime as dt
import time

#_____________creating a new Excel workbook_____________#

wb = xw.Book()              #Creates a new workbook
wb.save('experiment.xlsx')  #saves created workbook in the given path

wbExp = xw.Book('experiment2.xlsx') #opening an existing Excel file
wbBond = wbExp.sheets.add('Bonds', before='Equity', after='Forex') #creates a new worksheet in the spreadsheet
print(wbExp.sheets[2].name)         #prints the name of 3rd worksheet

#__________________Working with sheets___________________#

wbSum = wbExp.sheets['summary'] #assigning individual worksheets to variables
wbFx = wbExp.sheets['FOREX']    #one can pass sheet name or index number starting with 0
wbEq = xw.Book('experiment2.xlsx').sheets['Equity'] #another way

#__________________Writing to Excel file_________________#

wbSum.range('A1').value = 'Hello there'    #.range() takes a cell refrence or a range of cell refrence as a string
wbSum.range('A2:A21').value = 20

wbSum.cells(1, "B").value = 100            #.cells() takes rows & coloumns value as number and string or as numbers only
wbSum.cells(2, 2).value = 100              #.cells can be used for r/w only on 1 cell

#____Deleting values_____#
wbSum.clear()                              #Will clear the entire sheet with cell formating
wbSum.clear_contents()                     #Will clear the contents in all the cells leaving their formatting
wbSum.delete()                             #Delets the entire Sheet

wbSum.cells(1, 1).delete()                 #Clears the content, formatting & replaces with lower values
wbSum.cells(1, 1).clear()                  #Will clear the contants & formatting in the cell
wbSum.range(1, "B").clear_contents()       #Will clear only the contents in the given range

#__________________Reading from Excel file_________________#
coloumn = wbSum.range('A1:A21').value
print(coloumn)

print(wbFx.cells(1, 3).value)              #prints the value in 1st row 3rd coloumn

#____________Excel wings options & converters___________#

#ndim (number of dimentions)
print(wbSum.range('A1:B3').options(ndim=1).value)

#number
wbFx.range('A1').value = 100
print(wbFx.range('A1').value)                     #this returns a float
print(wbFx.range('A1').options(number=int).value) #this returns an int

#dates
print(wbFx.range('C1').value)
print(wbFx.range('C1').options(dates=dt.datetime.date).value) #while reading it will convert cell data to a datetime object
                                                              #while writing it will convert datetime object to excel date type

#empty
print(wbFx.range('A1:C1').value)                              #this will print empty cells as None
print(wbFx.range('A1:C1').options(empty='NA').value)          #this will print empty cells as the passed string

#transpose (only used while writing to file)
wbEq.range('A1').value = list(range(0, 10))                         #this writes data horizontaly from the range
wbEq.range('A1').options(transpose=True).value = list(range(0, 10)) #this writes data vertically from the range

#expand
data1 = wbEq.range('A1').expand().value                 #passes the values in range even after updaing the excel file
data2 = wbEq.range('A1').options(expand='table').value  #expand can be right or left, for vertical or horizontal only updates

print(data1)
print(data2)

# wbSum.cells.clear_contents()                          #clears entire worksheet
#_________________Iterative printing experiment_________________#

# while True:
#     for i in range(1, 100):
#         wbFx.range('B1').value = i
#         time.sleep(1)
# else: print('निकल')