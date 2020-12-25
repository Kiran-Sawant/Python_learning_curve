"""
ListBox: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/listbox.html
ScrollBar: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/scrollbar.html"""

import tkinter as tk

def select():
    """Prints users selection in ListBox on command-line.
    ListBox.curselection() returns a tuple of index, of users selection.
    ListBox.get(i) will return the values in listbox with those index."""
    try:
        cursor = lBox.curselection()[0]     # retriving first selection of user.
        selection = lBox.get(cursor)
    except IndexError:
        print("No Selection!")
    else:
        print(selection)

# Initiating window
mainWindow = tk.Tk()
mainWindow.geometry('440x440')
mainWindow.title('Listbox & scrollbar')

#______________Populating a listbox______________#
"""Many widgets require a variable to function.
variables can be created using tk.Variable for general variables,
tk.IntVar for integer variables and tk.StrVar for string variables.
To populate a listbox one needs to pass an iterable to the variable,
therefore a general type of variable is needed."""

# Creating list
k = list(x for x in range(0, 100, 2))
# Creating a general variable
lBox_var = tk.Variable(mainWindow)
# Passing list to variable
lBox_var.set(value=k)

# Creating listbox & assigning variable
lBox = tk.Listbox(master=mainWindow, listvariable=lBox_var)

# Creating a vertical Scrollbar
"""command parameter takes ListBox on which to apply the ScrollBar.
yview for vertical & xview for horizontal scrolling."""
sBar = tk.Scrollbar(master=mainWindow, orient=tk.VERTICAL, command=lBox.yview)

# Makes the ScrollBar move with ListBox
# lBox["yscrollcommand"] = sBar.set
lBox.config(yscrollcommand=sBar.set)        # same as above.

# Creating a button for executing function
btun = tk.Button(mainWindow, command=select, text="Print Selection")

# Placing Widgets
lBox.grid(row=0, column=0, sticky='w')
sBar.grid(row=0, column=1, sticky='wns', padx=0)
btun.grid(row=1, column=0, sticky='nw')

mainWindow.mainloop()