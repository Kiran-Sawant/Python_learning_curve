# TODO Complete the code, it doesn't work.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('420x360')

def check(k):
    
    if k in values:
        return True
    else:
        return False

text_var = tk.StringVar()
values = ('Cat', 'Dog', 'Snake')
w = ttk.Combobox(root, textvariable=text_var, values=values, validate='all', validatecommand=(check, '%S'))
checkCom = w.register(check)
w.pack()

buton = ttk.Button(root, text='Print!', command=lambda: print(text_var.get()))
buton.pack()

root.mainloop()