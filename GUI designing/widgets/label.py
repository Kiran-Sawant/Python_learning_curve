import tkinter as tk

def change():

    if var.get() == 'Killer Bean':
        var.set('KungFu Panda')
    else:
        var.set('Killer Bean')

# Initiating window
mainWindow = tk.Tk()
mainWindow.geometry('440x440')
mainWindow.title('Label Example')

# creating a label
l1 = tk.Label(master=mainWindow, text="Hello ugly world!")
# placing a label
l1.grid(row=0, column=0)

#_______Making a Mutable Label__________#
"""Link a StringVar to a label to and use the .set()
method on the String Var to make the label, mutable"""
var = tk.StringVar()
var.set('Killer Bean')

l2 = tk.Label(master=mainWindow, textvariable=var)
l2.grid(row=1, column=0)

buton = tk.Button(master=mainWindow, text='change', command=change)
buton.grid(row=2, column=0)

mainWindow.mainloop()