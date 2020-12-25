"""
Menu has a default tearoff set to 1.
a dashed line will appear above the choices.
The user can click on this line to “tear off” the menu:
a new, separate, independent window appears containing the choices.
Set tearoff=0 to remove tear-off line.
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/menu.html"""

import tkinter as tk

master = tk.Tk()
master.geometry("360x420")

#_____________Menu Bar_______________#
# Creating a Menu-bar.
menuBar = tk.Menu(master=master)
# Displaying the Menu-bar onto our root window.
# master['menu'] = menuBar
master.config(menu=menuBar)             # same as above

# Creating a pulldown menu for our Menu-bar.
file = tk.Menu(menuBar, activeforeground='cyan', activebackground='black')
# adding menu items to our pulldown menu.
file.add_command(label='Save')
file.add_command(label='Exit', command=master.destroy)
# Adding the pulldown menu to our Menu-bar
menuBar.add_cascade(label='File', menu=file)

# Creating another pulldown menu.
edit = tk.Menu(menuBar, tearoff=0)
# adding menu item to our pulldown menu.
edit.add_command(label='Undo')
edit.add_command(label='Redo')
# Adding the pulldown menu to our Menu-bar.
menuBar.add_cascade(label='Edit', menu=edit)

master.mainloop()