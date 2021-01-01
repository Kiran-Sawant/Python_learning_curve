""" PanedWindow widget gives the application's user some control over how space is
divided up within the application.
    A PanedWindow is somewhat like a Frame: it is a container for child widgets.
    Each PanedWindow widget contains a horizontal or vertical stack of child widgets.
    Using the mouse, the user can drag the boundaries between the child widgets.
    https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/panedwindow.html"""

import tkinter as tk

root = tk.Tk()
root.geometry('360x360')
root.title('Paned Window')

#________Creating a PanedWindow_________#
# Creating a horizontally paned window.
p_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
p_window.config(relief=tk.SUNKEN, sashrelief=tk.RAISED, showhandle=True)
p_window.grid(row=0, column=0)

#________Adding child to PanedWindows________#
"""To add child widgets to a PanedWindow, create the child widgets as children
of the parent PanedWindow, but rather than using the .grid() method to register
them, use the .add() method on the PanedWindow."""

# Creating 1st child widget
k = list(x for x in range(0, 100, 2))
lBox_var = tk.Variable(p_window)
lBox_var.set(value=k)
listBox = tk.Listbox(p_window, listvariable=lBox_var)
p_window.add(listBox)                           # adding listbox to PanedWindow.

# Creating 2nd child widget
buton = tk.Button(p_window, text='Press me')
p_window.add(buton, height=30, sticky='n')      # height is specified in pixels

root.mainloop()