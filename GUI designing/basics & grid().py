import tkinter as tk

#________Initializing window________#
mainWindow = tk.Tk()                    #Initializing a master window
mainWindow.title('Hello Python')        #title of GUI window
mainWindow.geometry('1280x720+350+130') #size of window & offset from LHS and top. use '-' for RHS & bottom offseting

#_________Configuring columns__________#
"""https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter
    Weight of a column or a row determines how much new space that perticular row or
column will get if the window is expanded. eg. If in a window 3 columns have
weight of 1, 2, 3 and x amount of new space is created then the new space will be
divided in a ratio of 2:3 between column 2 & 3.
    If weight is not set, the rows/columns will not expand."""

mainWindow.columnconfigure(0, weight=1) 
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

#______________Creating widgets_______________#
label = tk.Label(mainWindow, text='Hello Ugly World')
leftFrame = tk.Frame(mainWindow)
canvas = tk.Canvas(leftFrame, relief='raised', borderwidth=2, bg='green')
rightFrame = tk.Frame(mainWindow)
button1 = tk.Button(rightFrame, text='button1', relief='raised')
button2 = tk.Button(rightFrame, text='button2', relief='flat')
button3 = tk.Button(rightFrame, text='button3', relief='groove')

#______placing the widgets_______#
label.grid(row=0, column=0)
leftFrame.grid(row=1, column=1)
canvas.grid(row=0, column=0)
rightFrame.grid(row=1, column=2, sticky='n')
button1.grid(row=0, column=0)                                         
button2.grid(row=1, column=0)                                    
button3.grid(row=2, column=0)

#_________.config() method_________#
leftFrame.config(relief='sunken', bg='black', borderwidth=2)   #.config() lets set the parameters after the widget is created
rightFrame.config(relief='sunken', bg='grey', borderwidth=2)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

#_______configuring columns in a frame_______#
rightFrame.columnconfigure(index=0, weight=1)
button2.grid(sticky='ew')

mainWindow.mainloop()
