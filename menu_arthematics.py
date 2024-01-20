from tkinter import *

base = Tk()
base.geometry("700x400")
base.title("operations")

mb = Menu(base)
ar = Menu(mb)
rl = Menu(mb)


def add():
    v1 = int(en1.get())
    v2 = int(en2.get())
    res = v1 + v2
    en3.delete(0, END)
    en3.insert(0, str(res))


def sub():
    v1 = int(en1.get())
    v2 = int(en2.get())
    res = v1 - v2
    en3.delete(0, END)
    en3.insert(0, str(res))


def mul():
    v1 = int(en1.get())
    v2 = int(en2.get())
    res = v1 * v2
    en3.delete(0, END)
    en3.insert(0, str(res))


def div():
    v1 = int(en1.get())
    v2 = int(en2.get())
    res = v1 / v2
    en3.delete(0, END)
    en3.insert(0, str(res))


def gre():
    v1 = int(en1.get())
    v2 = int(en2.get())
    if v1 > v2:
        en3.delete(0, END)
        en3.insert(0, str(v1))
    else:
        en3.delete(0, END)
        en3.insert(0, str(v2))


def less():
    v1 = int(en1.get())
    v2 = int(en2.get())
    if v1 < v2:
        en3.delete(0, END)
        en3.insert(0, str(v1))
    else:
        en3.delete(0, END)
        en3.insert(0, str(v2))


def equal():
    v1 = int(en1.get())
    v2 = int(en2.get())
    if v1 == v2:
        en3.delete(0, END)
        en3.insert(0, str(True))
    else:
        en3.delete(0, END)
        en3.insert(0, str(False))


def noteq():
    v1 = int(en1.get())
    v2 = int(en2.get())
    if v1 != v2:
        en3.delete(0, END)
        en3.insert(0, str(True))
    else:
        en3.delete(0, END)
        en3.insert(0, str(False))
def clear():
    en1.delete(0,END)
    en3.delete(0,END)
    en2.delete(0,END)

mb.add_cascade(menu=ar, label="Arthematics")
mb.add_cascade(menu=rl, label="Relational")

ar.add_command(label="Addition", command=add)
ar.add_command(label="Subtraction", command=sub)
ar.add_command(label="Multiplication", command=mul)
ar.add_command(label="Division", command=div)

rl.add_command(label="Greater", command=gre)
rl.add_command(label="Smaller", command=less)
rl.add_command(label="Equal to", command=equal)
rl.add_command(label="Not equal to", command=noteq)

lab1 = Label(base, text="Enter first number")
lab2 = Label(base, text="Enter second number")
lab3 = Label(base, text="Result is:")
en1 = Entry(base)
en2 = Entry(base)
en3 = Entry(base)
bt = Button(base, text="Clear",command=clear)

lab1.place(x="100", y="40")
lab2.place(x="100", y="80")
lab3.place(x="100", y="120")
en1.place(x="250", y="40")
en2.place(x="250", y="80")
en3.place(x="250", y="120")
bt.place(x="200", y="200")

base.configure(menu=mb)
base.mainloop()
