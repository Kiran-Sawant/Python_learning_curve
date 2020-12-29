"""https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry-scrolling.html"""

import tkinter as tk

root = tk.Tk()
root.title("EntryBox")
root.geometry('360x360')

name_Label = tk.Label(master=root, text="Enter your name")
name_Label.grid(row=0, column=0, padx=5)

entry_var = tk.StringVar()

entry = tk.Entry(master=root, textvariable=entry_var)
entry.grid(row=0, column=1)

scroll = tk.Scrollbar(master=root, orient=tk.HORIZONTAL, command=entry.xview)
scroll.grid(row=1, column=1, sticky='ew')
entry['xscrollcommand'] = scroll.set

btn = tk.Button(master=root, text="Print", command=lambda : print(entry_var.get()))
btn.grid(row=2, column=1)

root.mainloop()