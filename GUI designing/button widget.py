import tkinter as tk
from tkinter import ttk

#_____Initializing window_____#
mainW = tk.Tk()
mainW.geometry('640x480+350+130')
mainW['padx'] = 10

#____creating buttons_____#
b1 = tk.Button(mainW, text='Fuck me!', bd=2, bg='cyan', fg='black', activebackground='red', activeforeground='white')
b2 = tk.Button(mainW, text='Fuck me to!', bd=2, bg='cyan', activebackground='red', cursor='spraycan')

#_____placing buttons______#
b1.grid(row=0, column=0, padx=8)
b2.grid(row=0, column=1)

mainW.mainloop()