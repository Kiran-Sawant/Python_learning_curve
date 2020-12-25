"""This script creates popup windows on a button click."""

import tkinter as tk

class popUp(tk.Tk):
    
    def __init__(self):
        super().__init__()
        # popUp = tk.Tk()
        label = tk.Label(self, text="Hello Ugly World!")
        label.pack()
        button = tk.Button(self, text="Destroy", command=self.button_func)
        button.pack()
        self.mainloop()
    
    def button_func(self):
        
        self.destroy()

def button1():
    k = popUp()

mainWindow = tk.Tk()

mainWindow.geometry('360x360')

button = tk.Button(mainWindow, text="new Window", command=button1)
button.pack()

mainWindow.mainloop()