import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('420x360')

button = ttk.Button(root, text='Click me', command=lambda: print('Hello World'))
button.pack()

ch_Button = ttk.Checkbutton(root, text='Random Stuff')
ch_Button.pack()

entry = ttk.Entry(root, show='#')
entry.pack()





root.mainloop()