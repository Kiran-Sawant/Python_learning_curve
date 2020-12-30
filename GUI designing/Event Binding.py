"""Read this documentation:-
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/events.html
TODO complete the code"""

import tkinter as tk

root = tk.Tk()
root.geometry('420x360')

# var = tk.StringVar()
# var.set("KungFu Panda")

label = tk.Label(root, text='KungFu Panda')
label.pack()

root.mainloop()

# print(var.get())