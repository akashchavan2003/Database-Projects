from tkinter import *

root = Tk()
root.title("CALCULATOR")
root.geometry("300x400")

tex3 = Entry()
tex3.place(x="200", y="235")


def div():
    x = int(text.get())
    y = int(text2.get())
    print("the divsion is:", x / y)
    res = x / y
    tex3.delete(0, END)
    tex3.insert(0, str(res))


def mul():
    x = int(text.get())
    y = int(text2.get())
    print("the multiplication is:", x * y)
    res = x * y
    tex3.delete(0, END)
    tex3.insert(0, str(res))


def add():
    x = int(text.get())
    y = int(text2.get())
    print("the addition is", x + y)
    res = x + y
    tex3.delete(0, END)
    tex3.insert(0, str(res))


def sub():
    x = int(text.get())
    y = int(text2.get())
    print("The subtraction is", x - y)
    res = x - y
    tex3.delete(0, END)
    tex3.insert(0, str(res))


label = Label(root, text="ENTER FIRST VALUE", font=" Arial")
label.place(x="20", y="45")
label2 = Label(root, text="ENTER SECOND VALUE", font="Arial")
label2.place(x="20", y="90")
text = Entry()
text.place(x="300", y="48")
text2 = Entry()
text2.place(x="300", y="95")
btn1 = Button(root, text="ADD", command=add)
btn2 = Button(root, text="SUB", command=sub)
btn3 = Button(root, text="MUL", command=mul)
btn4 = Button(root, text="DIV", command=div)
btn1.place(x="40", y="150")
btn2.place(x="120", y="150")
btn3.place(x="200", y="150")
btn4.place(x="280", y="150")
btn1.config(bg="purple", font="arial", fg="black")
btn2.config(bg="purple", font="arial", fg="black")
btn3.config(bg="purple", font="arial", fg="black")
btn4.config(bg="purple", font="arial", fg="black")
label3 = Label(root, text="RESULT IS :", font="Arial")
label3.place(x="40", y="230")

root.mainloop()
