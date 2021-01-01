"""The Spinbox widget allows the user to select values from a given set.
The values may be a range of numbers, or a fixed set of strings.
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/spinbox.html"""

import tkinter as tk

root = tk.Tk()
root.geometry('360x360')

# SpinBox with integer values.
spinBox = tk.Spinbox(root, from_=1, to=10)
spinBox.pack()

# SpinBox with string values.
sBoxTuple = ('Cat', 'Dog', 'Snake')
spinBox_2 = tk.Spinbox(root, values=sBoxTuple)
spinBox_2.config(wrap=True)             # Makes the list cycle.
spinBox_2.pack()

# Printing the values of selection.
buton = tk.Button(root, text='Print', command=lambda: print(f'{spinBox.get()} {spinBox_2.get()}'))
buton.pack()

root.mainloop()
