from tkinter import *


root = Tk()

c = Canvas(root, width=500, height=500, background="yellow")
root.geometry("500x500")
c.pack()
for i in range(50, 500, 50):
    c.create_line(i, 10, i, 490)
    c.create_line(10, i, 490, i)

rect = c.create_rectangle(5, 5, 45, 45, fill="aqua")


def cbRight(event):
    print('Right')
    print(c.coords(rect))
    x1 = c.coords(rect)[0]
    y1 = c.coords(rect)[1]
    if (440 < x1 < 500 and 440 < y1 < 500):
        print(1)
    elif (x1 < 450):
        c.move(rect, 50, 0)
    elif (x1 >= 450 and y1 < 450):
        c.move(rect, -450, 50)
    elif (x1 >= 450 and y1 >= 450):
        c.move(rect, -450, -450)
    print(x1)


def cbLeft(event):
    x1 = c.coords(rect)[0]
    y1 = c.coords(rect)[1]
    if (x1 <= 5 and y1 <= 5):
        print(2)
    elif (x1 > 50):
        c.move(rect, -50, 0)
    elif (x1 < 50 and y1 > 50):
        c.move(rect, 450, -50)
    elif (x1 < 50 and y1 < 50):
        c.move(rect, 450, 450)

    print('left', c.coords(rect))


def cbUp(event):
    print('up')
    y1 = c.coords(rect)[1]
    if (y1 > 50):
        c.move(rect, 0, -50)
    print(y1)


def cbDown(event):
    print('Down')
    y1 = c.coords(rect)[1]
    if (y1 < 450):
        c.move(rect, 0, 50)
    print(y1)


root.bind('<Right>', cbRight)
root.bind('<Left>', cbLeft)
root.bind('<Up>', cbUp)
root.bind('<Down>', cbDown)

root.mainloop()
