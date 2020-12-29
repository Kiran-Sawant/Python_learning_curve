"""Text widgets are a much more generalized method for
handling multiple lines of text than the Entry widget.
Text widgets are pretty much a complete text editor in a window
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/text.html"""

import tkinter as tk

def retrive():
    """Retriving input from index 0 of line 1 (hence 1.0)
    to last - 1 character. The output includes a end line
    character, so use end-1c, end-nc will remove n characters
    from end."""

    input_ = t_box.get('1.0', index2='end-1c')
    print(input_)

root = tk.Tk()
root.title("TextBox")
root.geometry('440x420')

# Creating Text widget with undo functionality.
t_box = tk.Text(master=root, undo=True, bg='#fffdd0')
"""width is in characters, height in lines, wrap dictates how to
break line."""
t_box.config(width=50, height=24, bd=4, padx=3, wrap=tk.WORD)
t_box.pack()

btn = tk.Button(root, text='Print', command=retrive)
btn.pack()

root.mainloop()