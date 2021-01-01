"""https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/message.html"""

import tkinter as tk 

# Retriving the string for message.
# __file__ returns path of this script
path = __file__.replace('Message 2.py', 'sample.txt')
with open(path, mode='r') as text_file:
    lyrics = text_file.read()
    # print(lyrics)

root = tk.Tk()
root.geometry('300x620')
root.title('Message widget')

msg = tk.Message(master=root, text=lyrics)
msg.pack()

msg.config(bg='#fffdd0')        # setting background colour

root.mainloop()
