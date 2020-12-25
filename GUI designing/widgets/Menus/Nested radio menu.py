"""
Each radiobutton in a group must have a unique value option of the same type
as the control variable. For example, a group of three radiobuttons might share
an IntVar and have values of 0, 1, and 99.
Create IntVar if radioButtons indicate integer values & StringVar if string."""

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

#____________Creating a RadioButton menu_____________#
# Creating a tk variable for radio button.
vari = tk.StringVar()

radio = tk.Menu(master=file_tab)
radio.add_radiobutton(label="Dog", value='Dog', variable=vari)
radio.add_radiobutton(label="Cat", value='Cat', variable=vari)
radio.add_radiobutton(label="Snake", value='Snake', variable=vari)

file_tab.add_cascade(label='Radio', menu=radio)

# Creating a button
bton = tk.Button(master=root, text='Print Pet', command=lambda : print(vari.get()))
bton.pack()

root.mainloop()