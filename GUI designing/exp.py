import tkinter as tk

mainWindow = tk.Tk()
mainWindow.geometry('640x480')
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(1, weight=1)

frameOne = tk.Frame(mainWindow, bg='grey', borderwidth=1)
frameOne.grid(row=0, column=0)

button = tk.Button(frameOne, width=10, text='new')
button.grid(row=0, column=0)

frameTwo = tk.Frame(mainWindow, bg='green', borderwidth=2)
frameTwo.grid(row=0, column=1)

button2 = tk.Button(frameTwo, width=10,  text='new')
button2.grid(row=0, column=0)

frameThree = tk.Frame(mainWindow, bg='yellow', borderwidth=1)
frameThree.grid(row=0, column=2)

button3 = tk.Button(frameThree, width=10, text='new')
button3.grid(row=0, column=0)

mainWindow.mainloop()