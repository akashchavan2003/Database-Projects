from tkinter import *
import random

flag1 = 0
base = Tk()
base.geometry("700x400")
tex1 = Label(base)
text = Label(base)
text.place(x="300", y="100")
tex1.place(x="400", y="300")


def random1():
    v1 = random.randint(11, 17)
    return v1


rn = random1()


def display(num):
    global flag1
    global v1

    if flag1 == 0:
        v1 = num
        text.config(text=str(num))
        flag1 = 1
    else:
        total = v1 + num
        text.config(text=str(total))
        if total == rn:
            tex1.config(text="CORRECT!")
        else:
            tex1.config(text="TRY AGAIN!")
            text.config(text="")


def clear():
    text.config(text="")


btn1 = Button(base, text="1", bg="purple", width=10, height=2, fg="white", command=lambda: display(1))
btn2 = Button(base, text="2", bg="purple", width=10, height=2, fg="white", command=lambda: display(2))
btn3 = Button(base, text="3", bg="purple", width=10, height=2, fg="white", command=lambda: display(3))
btn4 = Button(base, text="4", bg="purple", width=10, height=2, fg="white", command=lambda: display(4))
btn5 = Button(base, text="5", bg="purple", width=10, height=2, fg="white", command=lambda: display(5))
btn6 = Button(base, text="6", bg="purple", width=10, height=2, fg="white", command=lambda: display(6))
btn7 = Button(base, text="7", bg="purple", width=10, height=2, fg="white", command=lambda: display(7))
btn8 = Button(base, text="8", bg="purple", width=10, height=2, fg="white", command=lambda: display(8))
btn9 = Button(base, text="9", bg="purple", width=10, height=2, fg="white", command=lambda: display(9))
btn0 = Button(base, text="0", bg="purple", width=10, height=2, fg="white", command=lambda: display(0))
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
btn0.grid(row=3, column=1)
label = e = Label(text="Press Two Buttons For Addition Of Below NO.")
label.place(x="330", y="45")
label.config(bg="white")  # Adjust color as needed
label.config(fg="black")
label.config(font=("Arial", 12))

label2 = Label(text=rn)
label2.place(x="450", y="80")
label2.config(font=("Arial", 30))

bt = Button(base, text="clear", command=clear)
bt.place(x="600", y="150")
base.mainloop()
