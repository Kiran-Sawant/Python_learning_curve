""" Frame widgets are a valuable tool in making your application modular. You can group a set of related
widgets into a compound widget by putting them into a frame. Better yet, you can declare a new class
that inherits from Frame, adding your own interface to it. This is a good way to hide the details
of interactions within a group of related widgets from the outside world.
    This script impliments Frames using object oriented programming.
    The MyFrame class represents a Frame that contains related widgets, this frame can be added to any window.
    The Popup class inherits from the Tk class and therefore each of its instance creates its own independent
window, each Popup object contains a MyFrame object, therefore our defined Frame will be displayed in each of
its instances."""

import tkinter as tk

class MyFrame(tk.Frame):
    """Defines a tk Frame containing related widgets"""
    def __init__(self, master: tk.Tk):
        super().__init__(master)

        self.grid(row=0, column=0, padx=5)
        self['cursor'] = 'circle'
        self.my_label = tk.Label(self, text = 'Hello World')
        self.my_button = tk.Button(self, text='Change', command=self.change)

        self.my_button.grid(row=1, column=0)
        self.my_label.grid(row=0, column=0)
    
    def change(self):
        """Changes the text of the label"""

        if self.my_label['text'] == 'Hello World':
            self.my_label['text'] = 'Hello Ugly World'
        else:
            self.my_label['text'] = 'Hello World'

class Popup(tk.Tk):
    """Creates a new independent tk window"""
    
    def __init__(self):
        super().__init__()
        self.geometry('160x160')
        self.title('PopUp')

        pop_frame = MyFrame(self)

        self.mainloop()

root = tk.Tk()
root.geometry('360x360')
root.title('Frames with OOP')

frame = MyFrame(root)

button = tk.Button(root, text='new window', command=lambda: Popup())
button.grid(row=1, column=0)

root.mainloop()