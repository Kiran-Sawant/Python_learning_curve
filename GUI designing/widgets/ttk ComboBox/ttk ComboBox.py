"""This widget is a combination of an Entry and a drop-down menu.
In your application, you will see the usual text entry area, with
a downward-pointing arrow. When the user clicks on the arrow, a
drop-down menu appears. If the user clicks on one, that choice
replaces the current contents of the entry. However, the user may
still type text directly into the entry (when it has focus), or
edit the current text."""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('420x360')



text_var = tk.StringVar()
values = ('Cat', 'Dog', 'Snake')
w = ttk.Combobox(root, textvariable=text_var, values=values)
w.pack()

buton = ttk.Button(root, text='Print!', command=lambda: print(text_var.get()))
buton.pack()

root.mainloop()