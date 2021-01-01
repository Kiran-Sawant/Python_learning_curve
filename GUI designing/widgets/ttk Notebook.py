"""The purpose of a Notebook widget is to provide an
area where the user can select pages of content by
clicking on tabs at the top of the area.
The widget in each tab is generaly a Frame with all the
widgets setup properly."""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('360x360')
root.title("ttk Notebook")

nBook = ttk.Notebook(root)
nBook.pack()

can = tk.Canvas(nBook)
buton = ttk.Button(nBook, text='Press')
etxt = tk.Text(nBook)

nBook.add(can, text='Canvas')
nBook.add(buton, text='Button')
nBook.add(etxt, text='Editor')

root.mainloop()