"""
The LabelFrame widget, like the Frame widget, is a spatial container—a rectangular
area that can contain other widgets. However, unlike the Frame widget, the LabelFrame
widget allows you to display a label as part of the border around the area.
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/labelframe.html"""

import tkinter as tk

root = tk.Tk()
root.geometry('360x360')
root.title("Labeled Frames")

# Creating the Labeled Frame
frame_1 = tk.LabelFrame(root, text='Buttons')
frame_1.grid(row=0, column=0, padx=5, pady=5)

# Creating the widgets to be placed in the frame
button_1 = tk.Button(frame_1, text='Press')
button_1.grid(row=0, column=0)

button_2 = tk.Button(frame_1, text='Press')
button_2.grid(row=0, column=1, padx=20)

root.mainloop()