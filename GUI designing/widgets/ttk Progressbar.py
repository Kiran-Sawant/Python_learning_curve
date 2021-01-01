"""https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Progressbar.html"""

import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.geometry('420x360')

var = tk.IntVar()

w = ttk.Progressbar(root, mode='determinate', variable=var, maximum=100)
w.pack()

w.start()
f = 0
while f == 100:

    # w.step(5.0)
    if f == 80:
        w.stop()
        time.sleep(10)
        w.start()
    var.set(f)
    time.sleep(1)
    f += 5

# w.stop()

root.mainloop()