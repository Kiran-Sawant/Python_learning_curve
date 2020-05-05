import tkinter as tk

keys = [[('C',  1), ('CE', 1)],                     #making a list of all keys with its colspan
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)]]

mainWindowPadding = 8

mainWindow = tk.Tk()
mainWindow.title('Calculator')
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

result = tk.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

keyPad = tk.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for  keyRow in keys:
    col = 0
    for key in keyRow:
        tk.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tk.E + tk.W)
        col += 1
    row += 1

#__________________For keeping the size of the window fixed______________________#
mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())

tk.mainloop()
