"""
Every Menu object has a .add_cascade() method that can
be used to nest a child Menu into a parent Menu.
Pass the child Menu to the menu parameter of .add_cascade()
method of the parent Menu (line 34)."""

import tkinter as tk

# Initializing root window
root = tk.Tk()
root.geometry("360x420")
root.title("Nested Menus")

#___________Menu Bar____________#
menu_bar = tk.Menu(root)            # Creating Menu-bar.
root['menu'] = menu_bar             # display menu-bar on master window.

# Creating pulldown menus for Menu-bar.
file_tab = tk.Menu(master=menu_bar)
help_tab = tk.Menu(master=menu_bar)

# Display pulldown menus on Menu-bar.
menu_bar.add_cascade(label='File', menu=file_tab)
menu_bar.add_cascade(label='help', menu=help_tab)

# Creating a sub menu for file tab
option = tk.Menu(master=file_tab)
# adding items in sub menu
option.add_command(label="Option 1", command=lambda : print('Option 1'))
option.add_command(label="Option 2", command=lambda : print('Option 2'))
option.add_command(label="Option 3", command=lambda : print('Option 3'))

# adding option in file_tab
file_tab.add_cascade(label='Option', menu=option)

root.mainloop()