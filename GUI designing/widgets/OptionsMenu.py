"""
    OptionsMenu requires an iterable to be passed in the *values parameter
of the OptionMenu constructor.
    The Option you select in the OptionMenu will be assigned to a tk
variable which is needed to be instantiated before OptionsMenu.
    Make the tk variable of the same type as that of the contants of the
iterable.
    Do not mention the Identifiers of the parameters."""

import tkinter as tk

root = tk.Tk()
root.geometry('360x360')
root.title('OptionMenu')

# Options for Options Menu.
Op_list = ['Dog', 'Cat', 'Snake']

# Creating variable for OptionsMenu.
Op_var = tk.StringVar()
Op_var.set(Op_list[0])      # setting default value

# Creating OptionMenu Widget.
Op_menu = tk.OptionMenu(root, Op_var, *Op_list)
Op_menu.pack()

root.mainloop()
