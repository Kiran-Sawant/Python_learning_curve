import tkinter as tk
import os

mainWindow = tk.Tk()                     #Initializing a master window

mainWindow.title('Grid Demo')            #title of GUI window
mainWindow.geometry('640x480+350+130')   #Resolution and offset
mainWindow['padx'] = 8

label = tk.Label(mainWindow, text="Tkinter Grid demo")  #Window label
label.grid(row=0, column=0, columnspan=3, sticky='n')

#__________Configuring all the columns & rows in main window__________#
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

#___________List Box___________#
fileList = tk.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.configure(borderwidth=4, relief='flat')
for zone in os.listdir(r'C:\Windows\System32'):
    fileList.insert(tk.END, zone)
#________List box scroller________#
scroller = tk.Scrollbar(mainWindow, orient=tk.VERTICAL, command=fileList.yview) 
scroller.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = scroller.set

#___________frame for radio buttons________#
optionFrame = tk.LabelFrame(mainWindow, text='File Details', borderwidth=4)
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tk.IntVar()   #variable for radio buttons
rbValue.set(1)          #default value for radio button

#___________radio Buttons___________#
radio1 = tk.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tk.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3 = tk.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=2, column=0, sticky='w')
radio3.grid(row=3, column=0, sticky='w')

#__________Entry widget to display the result__________#
resulLabel = tk.Label(mainWindow, text='Result')
resulLabel.grid(row=2, column=2, sticky='nw')
result = tk.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

#______frame for time spinner______#
timeFrame = tk.LabelFrame(mainWindow, text='Time', borderwidth=2)
timeFrame.grid(row=3, column=0, sticky='new')
#_______time spinners________#
hourSpinner = tk.Spinbox(timeFrame, width=2, value=tuple(range(0, 24)))
minuteSpinner = tk.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tk.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
minuteSpinner.grid(row=0, column=1)
secondSpinner.grid(row=0, column=2)
timeFrame['padx'] = 80

#_______Frame for date spinners_________#
dateFrame = tk.LabelFrame(mainWindow, text='Date', borderwidth=2)
dateFrame.grid(row=4, column=0, sticky='new')

#_______Date Labels________#
dayLabel = tk.Label(dateFrame, text='Day')
monthLabel = tk.Label(dateFrame, text='Month')
yearLabel = tk.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

#______Date Spinners_______#
daySpin = tk.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tk.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
yearSpin = tk.Spinbox(dateFrame, width=5, from_=2000, to=2030)
daySpin.grid(row=1, column=0, sticky='w')
monthSpin.grid(row=1, column=1, sticky='w')
yearSpin.grid(row=1, column=2, sticky='w')
dateFrame['padx'] = 40

#_______________Buttons________________#
okButton = tk.Button(mainWindow, text='OK')
cButton = tk.Button(mainWindow, text='Quit', command=mainWindow.destroy) #.destroy kills all the windows
okButton.grid(row=4, column=3, sticky='e')
cButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()
