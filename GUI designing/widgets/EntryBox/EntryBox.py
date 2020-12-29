"""https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry.html"""

import tkinter as tk

# def switch():
#     if entry['state'] == tk.DISABLED:
#         entry['state'] = tk.NORMAL
#     else:
#         entry['state'] = tk.DISABLED

root = tk.Tk()
root.title("EntryBox")
root.geometry('360x360')

name_Label = tk.Label(master=root, text="Enter your name")
name_Label.grid(row=0, column=0, padx=5)

entry_var = tk.StringVar()

entry = tk.Entry(master=root, textvariable=entry_var)
entry.grid(row=0, column=1)

btn = tk.Button(master=root, text="Print", command=lambda : print(entry_var.get()))
btn.grid(row=1, column=1)

root.mainloop()

# print(entry_var.get())