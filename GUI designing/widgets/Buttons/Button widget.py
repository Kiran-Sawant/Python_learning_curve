"""Creating a Tk window with 2 buttons with different properties."""

import tkinter as tk

#_____Initializing window_____#
mainW = tk.Tk()
mainW.geometry('640x480+350+130')
mainW['padx'] = 10

#____creating buttons_____#
b1 = tk.Button(mainW, text='Fuck me!')
b2 = tk.Button(mainW, text='Fuck me too!')

#_____placing buttons______#
b1.grid(row=0, column=0, padx=8)
b2.grid(row=0, column=1)

#_____Configuring buttons______#
""" .config() can be used to add trivial details of the widget after they are created.
bd: border, bg: Background, fg: foreground."""

b1.config(bd=2, bg='cyan', fg='black', activebackground='red', activeforeground='white')
b2.config(bd=10, bg='cyan', activebackground='red', cursor='spraycan')

mainW.mainloop()