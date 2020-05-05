import tkinter as tk

print(tk.TkVersion)     #gives tkinter version
print(tk.TclVersion)    #gives version of TCL binding

# tk._test()              #pops a test GUI window

mainWindow = tk.Tk()      #Initializing a master window

mainWindow.title('Hello Python')        #title of GUI window
mainWindow.geometry('1280x720+350+130') #size of window & offset from LHS and top. use '-' for RHS & bottom offseting

label = tk.Label(mainWindow, text='Hello Ugly World')             #creates text labels
label.pack(side='top')                                            #places the object on top of masterwindow

leftFrame = tk.Frame(mainWindow, bg='grey', borderwidth=2)        #Creates a child space in the master window 
leftFrame.pack(side='left', anchor='n', fill=tk.Y, expand=False)  #places the Frame to the left of master, anchored to the north, filling the entire Y axis

canvas = tk.Canvas(leftFrame, relief='raised', borderwidth=2)     #Canvas is used to display graphical elements like line, graphs, etc
canvas.pack(side='right', anchor='n')                             #placing the Canvas to the right 0f master

rightFrame = tk.Frame(mainWindow, bg='grey', borderwidth=2)
rightFrame.pack(side='right', anchor='n', expand=True)            #exand allows the Frame to strech acording to the widgets in it

button1 = tk.Button(rightFrame, text='button')                   #creates a button widget in its master with the text written in it
button2 = tk.Button(rightFrame, text='button2')
button3 = tk.Button(rightFrame, text='button3')
button1.pack(side='left')                                         #button1 is placed in the extreame left of master
button2.pack(side='left')                                         #here, button2 is palced on left of button1 & button3 is packed on left of button2
button3.pack(side='left')

mainWindow.mainloop()