"""
A frame is basically just a container for other widgets.
Your application's root window is basically a frame.
Each frame has its own grid layout, so the gridding of widgets within each
frame works independently."""

import tkinter as tk

root = tk.Tk()
root.geometry('360x360')
root.title("tkinter Frames")

frame_1 = tk.Frame(root, bd=2, cursor='fleur', relief=tk.GROOVE)
frame_1.grid(row=0, column=0, padx=5, pady=5)

frame_2 = tk.Frame(root, bd=2, cursor='circle', relief=tk.RAISED)
frame_2.grid(row=0, column=1, padx=5, pady=5)

button_1 = tk.Button(frame_1, text='Press')
button_1.pack()

button_2 = tk.Button(frame_2, text='Press')
button_2.pack()

root.mainloop()