"""Creating a Tk window with 3 buttons in 3 different frames.
3 frames each in 3 columns with different weight."""

import tkinter as tk

mainWindow = tk.Tk()                        # Initializing main Window
mainWindow.geometry('640x480')              # Giving dimentions
mainWindow.columnconfigure(2, weight=3)     # Configuring 3rd column
mainWindow.columnconfigure(1, weight=2)     # Configuring 2rd column

#_________Creating Widgets___________#
frameOne = tk.Frame(mainWindow, bg='grey', borderwidth=1)       # bg: Background
frameTwo = tk.Frame(mainWindow, bg='green', borderwidth=2)
frameThree = tk.Frame(mainWindow, bg='yellow', borderwidth=1)
button = tk.Button(frameOne, width=10, text='Killer')
button2 = tk.Button(frameTwo, width=10,  text='Bean')
button3 = tk.Button(frameThree, width=10, text='Forever')

#_________Placing the widgets_________#
frameOne.grid(row=0, column=0)
frameTwo.grid(row=0, column=1)
frameThree.grid(row=0, column=2)
button.grid(row=0, column=0)
button2.grid(row=0, column=0)
button3.grid(row=0, column=0)

mainWindow.mainloop()