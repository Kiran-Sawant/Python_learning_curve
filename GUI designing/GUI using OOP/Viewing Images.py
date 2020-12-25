import tkinter as tk
from PIL import Image, ImageTk

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(tk.Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        tk.Frame.__init__(self, master)

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=tk.BOTH, expand=1)

        # creating a button instance
        # quitButton = tk.Button(self, text="Exit",command=self.client_exit)

        # placing the button on my Frame
        # quitButton.place(x=0, y=0)

        #_____________Menu Bar_______________#
        # Creating a Menu-bar.
        menuBar = tk.Menu(master=self.master)
        # Displaying the Menu-bar onto our root window.
        self.master.config(menu=menuBar)

        # Creating a pulldown menu for our menubar.
        file = tk.Menu(menuBar)
        # adding menu items to our pulldown menu.
        file.add_command(label='Save', command=self.client_exit)
        file.add_command(label='Exit', command=self.client_exit)
        # Adding the pulldown menu to our Menu-bar
        menuBar.add_cascade(label='File', menu=file)

        # Creating another pulldown menu.
        edit = tk.Menu(menuBar)
        # adding menu item to our pulldown menu.
        edit.add_command(label='Show Image', command=self.show_img)
        edit.add_command(label='Show Text', command=self.show_txt)
        # Adding the pulldown menu to our Menu-bar.
        menuBar.add_cascade(label='Edit', menu=edit)
       
    def show_img(self):

        load = Image.open(r"H:\Images\Bruce Lee.jpg")
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def show_txt(self):

        text = tk.Label(self, text='Hey Yo!')
        text.pack()

    def client_exit(self):
        exit()

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = tk.Tk()

root.geometry("400x300")

#creation of an instance
app = Window(master=root)

#mainloop 
root.mainloop()