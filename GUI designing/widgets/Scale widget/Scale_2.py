"""The command parameter of the scale widget executes the given function whenever
the slider is moved and passes the new slider value as argument. If the slider is
moved very rapidly it will pass the value where the slider stoped."""

import tkinter as tk

root = tk.Tk()
root.geometry('360x360')

# scale_var = tk.IntVar()
scale = tk.Scale(root, from_=0, to=10, resolution=1.0, orient=tk.HORIZONTAL)
"""here, command parameter executes the lambda function and passes the scale value
on every scale movement."""
scale.config(sliderlength=25, length=200, command=lambda x: print(x))
scale.pack()



root.mainloop()