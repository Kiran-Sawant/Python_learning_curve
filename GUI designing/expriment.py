import tkinter as tk
from tkinter import filedialog

file = None

def selector():
    global file

    file = filedialog.asksaveasfile(filetypes=[('Excel File', '*.xlsx')])


def printer():
    global file

    with open(file, 'r') as text:
        print(text.read())

def saver():
    global file

    directory = filedialog.askdirectory()

    text = open(directory + 'poetry.txt', 'w')

    for line in file.readline():
        print(line, file=text)
        print("Penis", file=text)

    text.close()

mainW = tk.Tk()
mainW.geometry('240x360')

button = tk.Button(mainW, text="Selector", command=selector)
button.pack()

button_2 = tk.Button(mainW, text="Print me", command=printer)
button_2.pack()

button_3 = tk.Button(mainW, text="Save me", command=saver)
button_3.pack()

mainW.mainloop()

print(file.name)