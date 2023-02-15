from tkinter import *


root = Tk()

c = Canvas(root, width=500, height=500, background="yellow")
root.geometry("500x500")
c.pack()
for i in range(50, 500, 50):
    c.create_line(i, 10, i, 490)
    c.create_line(10, i, 490, i)

kvadrat = c.create_rectangle(5, 5, 45, 45, fill="aqua")


def cbRight(event):
    print('Right')
    print(c.coords(kvadrat))
    x0 = c.coords(kvadrat)[0]
    if (x0 < 450):
        c.move(kvadrat, 50, 0)
    print(x0)


def cbLeft(event):
    print('Left')
    x0 = c.coords(kvadrat)[0]
    if (x0 > 50):
        c.move(kvadrat, -50, 0)
    print(x0)


def cbUp(event):
    print('up')
    y0 = c.coords(kvadrat)[1]
    if (y0 > 50):
        c.move(kvadrat, 0, -50)
    print(y0)


def cbDown(event):
    print('Down')
    y0 = c.coords(kvadrat)[1]
    if (y0 < 450):
        c.move(kvadrat, 0, 50)
    print(y0)


root.bind('<Right>', cbRight)
root.bind('<Left>', cbLeft)
root.bind('<Up>', cbUp)
root.bind('<Down>', cbDown)

root.mainloop()
