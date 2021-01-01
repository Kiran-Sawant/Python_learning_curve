"""The purpose of a scale widget is to allow the user to set some int
or float value within a specified range, using a slider.
Scale widget needs a binded IntVar to retrive the value.
Scale wiget can only be applied on a range of integers.
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/scale.html"""

import tkinter as tk

root = tk.Tk()
root.geometry('360x360')
root.title('Scale')

scale_var = tk.IntVar()
scale = tk.Scale(root, from_=0, to=10, resolution=1.0, orient=tk.HORIZONTAL, variable=scale_var)
scale.config(sliderlength=25, length=200)
scale.pack()

buton = tk.Button(root, text="print", command=lambda: print(scale_var.get()))
buton.pack()

root.mainloop()