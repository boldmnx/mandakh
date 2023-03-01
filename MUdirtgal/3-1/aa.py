from tkinter import *


def cbUp(event):
    y1 = c.coords(rect)[1]
    if (y1 > 50):
        c.move(rect, 0, -50)

    print('up', c.coords(rect))


def cbDown(event):
    y1 = c.coords(rect)[1]
    if (y1 < 450):
        c.move(rect, 0, 50)
    elif (y1 > 450):
        c.move(rect, 50, -450)
    elif (y1 < 0 and x < 450):
        c.move(rect, -50, 450)

    print('down', c.coords(rect))


def cbRight(event):
    x1 = c.coords(rect)[0]
    y1 = c.coords(rect)[1]
    if (440 < x1 < 500 and 440 < y1 < 500):
        print(1)

    if (x1 < 450):
        c.move(rect, 50, 0)
    elif (x1 >= 450 and y1 < 450):
        c.move(rect, -450, 50)
    elif (x1 >= 450 and y1 >= 450):
        c.move(rect, -450, -450)
    print('right', c.coords(rect))


def cbLeft(event):
    x1 = c.coords(rect)[0]
    y1 = c.coords(rect)[1]
    if (x1 > 50):
        c.move(rect, -50, 0)
    elif (x1 < 50 and y1 > 50):
        c.move(rect, 450, -50)
    elif (x1 < 50 and y1 < 50):
        c.move(rect, 450, 450)

    print('left', c.coords(rect))


root = Tk()
root.geometry("500x500")

c = Canvas(root, width=500, height=500, background="white")
c.pack()

for i in range(50, 500, 50):
    c.create_line(i, 10, i, 490)
    c.create_line(10, i, 490, i)

rect = c.create_rectangle(5, 5, 45, 45, fill="aqua")

root.bind('<Up>', cbUp)
root.bind('<Down>', cbDown)
root.bind('<Right>', cbRight)
root.bind('<Left>', cbLeft)
root.mainloop()
