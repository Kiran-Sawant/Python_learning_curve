import tkinter as tk

def parabola(x):
    y = x * x/100
    return y

def draw_axis(graph):
    graph.update()
    x_origin = graph.winfo_width()/2
    y_origin = graph.winfo_height()/2
    graph.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    graph.create_line(-x_origin, 0, x_origin, 0, fill='black')
    graph.create_line(0, -y_origin, 0, y_origin, fill='black')

def plot(canvas, x, y):
    canvas.create_line(x, y, x+1, y+1, fill='red')

mainWindow = tk.Tk()
mainWindow.title('Parabola')
mainWindow.geometry('640x480')

canvas = tk.Canvas(mainWindow, width=320, height=480)
canvas.grid(row=0, column=0)

canvas2 = tk.Canvas(mainWindow, width=320, height=480, background='grey')
canvas2.grid(row=0, column=1)

draw_axis(canvas)
draw_axis(canvas2)

for x in range(-1000, 1000):
    y = parabola(x)
    plot(canvas, x, -y)
    plot(canvas2, -x, y)

mainWindow.mainloop()