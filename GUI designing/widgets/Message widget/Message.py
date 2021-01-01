"""Message widget is similar to the Label widget, but it is intended
for displaying messages over multiple lines. All the text will be
displayed in the same font.
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/message.html"""

import tkinter as tk

# Retriving the string for message.
with open('sample.txt', mode='r') as text_file:
    lyrics = text_file.read()
    # print(lyrics)

root = tk.Tk()
root.geometry('360x420')
root.title('Message widget')

msg = tk.Message(master=root, text=lyrics)
msg.pack()

root.mainloop()