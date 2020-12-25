"""
The Items in a Menu object can be a cascade, check-box, radio-button, or a button.
CheckBoxes require a IntVar object associated with them, every checkbox item requires
an associated IntVar object, added using "variable" parameter.
IntVar is assigned 0 if that CheckBox is unchecked & 1 if it is checked.
use .get() getter method of IntVar to retrive values.

This script prints the checked values in the pets CheckBox menu in the File pulldown menu
on the button press."""

import tkinter as tk

def checkthebox():
    """Prints the checked items onto console."""

    # list of IntVar values after checking.
    selection = [var1.get(), var2.get(), var3.get()]
    # list of associated CheckBox values.
    pets=['Cat', 'Dog', 'Snake']
    sel_tup = tuple(zip(selection, pets))
    # print(sel_tup)
    for i in sel_tup:
        if i[0] == 1: print(i[1])
        else: continue

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
option.add_command(label="Option 1")
option.add_command(label="Option 2")
option.add_command(label="Option 3")

# adding option-menu in file_tab-menu
file_tab.add_cascade(label='Option', menu=option)

#_________Creating checkBox sub-menu__________#
check = tk.Menu(master=file_tab)

# Creating control variables
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

# Creating check buttons to checkBox menu
check.add_checkbutton(label='Cat', variable=var1)
check.add_checkbutton(label='Dog', variable=var2)
check.add_checkbutton(label='Snake', variable=var3)
# Adding checkBox menue to file-tab menu
file_tab.add_cascade(label="Pets", menu=check)

# Creating a button to retrive selected values
button = tk.Button(root, text='Print Pet selection', command=checkthebox)
button.pack()

root.mainloop()