import tkinter as tk
import math

def parabola(page, size):
    for x in range(size):
        y = x * (x/size)
        plot(page, x, y)
        plot(page, -x, y)
        plot(page, -x, -y)
        plot(page, x, -y)


def circle(page, radius, g, h, color='red'):
    for x in range(g * 100, (g + radius) * 100):
        x/=100
        y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
        plot(page, x, y, color)
        plot(page, x, 2 * h - y, color)
        plot(page, 2 * g - x, y, color)
        plot(page, 2 * g - x, 2 * h - y, color)


def draw_axis(graph):
    graph.update()
    x_origin = graph.winfo_width()/2
    y_origin = graph.winfo_height()/2
    graph.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    graph.create_line(-x_origin, 0, x_origin, 0, fill='black')
    graph.create_line(0, -y_origin, 0, y_origin, fill='black')


def plot(page, x, y, color='red'):
    page.create_line(x, -y, x+1, -y+1, fill=color)

mainWindow = tk.Tk()
mainWindow.title('Parabola')
mainWindow.geometry('640x480')

canvas = tk.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# canvas2 = tk.Canvas(mainWindow, width=320, height=480, background='grey')
# canvas2.grid(row=0, column=1)

draw_axis(canvas)
# draw_axis(canvas2)

parabola(canvas, 200)
circle(canvas, 100, 100, 100, color='green')
circle(canvas, 100, 100, -100, color='yellow')
circle(canvas, 100, -100, 100, color='cyan')
circle(canvas, 100, -100, -100)

mainWindow.mainloop()