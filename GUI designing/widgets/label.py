import tkinter as tk

# Initiating window
mainWindow = tk.Tk()
mainWindow.geometry('440x440')
mainWindow.title('Label Example')

# creating a label
l1 = tk.Label(master=mainWindow, text="Hello ugly world!")
# placing a label
l1.pack()

mainWindow.mainloop()