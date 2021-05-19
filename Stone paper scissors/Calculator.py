from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x500")
root.maxsize(300,500)
root.minsize(300,500)
root.configure(background='light blue')
def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())

            except Exception as e:
                value = "E R R O R"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue, font="Garamound 40 italic")
screen.pack(fill=X, padx=8, pady=10, ipadx=10)

f1 = Frame(root, bg="light blue")

b2 = Button(f1, text="C", padx=40, pady=10, font="Times 20 bold")
b2.pack(side=LEFT, padx=5, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(f1, text="=", padx=10, pady=10, font="Times 20 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)

b3 = Button(f1, text="+", padx=10, pady=10, font="Times 20 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)

f1.pack()
f1 = Frame(root,bg="light blue")
b1 = Button(f1, text="9", padx=10, pady=10, font="Times 20 bold")
b1.pack(side=LEFT, padx=5, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(f1, text="8", padx=10, pady=10, font="Times 20 bold")
b2.pack(side=LEFT, padx=5, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(f1, text="7", padx=10, pady=10, font="Times 20 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)

b3 = Button(f1, text="-", padx=10, pady=10, font="Times 20 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root,bg="light blue")
b1 = Button(f1, text="6", padx=10, pady=10, font="Times 20 bold")
b1.pack(side=LEFT, padx=5, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(f1, text="5", padx=10, pady=10, font="Times 20 bold")
b2.pack(side=LEFT, padx=5, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(f1, text="4", padx=10, pady=10, font="Times 20 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)

b3 = Button(f1, text="*", padx=10, pady=10, font="Times 20 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)

f1.pack()

f1 = Frame(root,bg="light blue")
b1 = Button(f1, text="3", padx=10, pady=10, font="Times 20 bold")
b1.pack(side=LEFT, padx=5, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(f1, text="2", padx=10, pady=10, font="Times 20 bold")
b2.pack(side=LEFT, padx=5, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(f1, text="1", padx=10, pady=10, font="Times 20 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)

b1 = Button(f1, text=".", padx=10, pady=10, font="Times 20 bold")
b1.pack(side=LEFT, padx=5, pady=5)
b1.bind("<Button-1>", click)


f1.pack()

f1 = Frame(root,bg="light blue")
b1 = Button(f1, text="%", padx=12, pady=20, font="Times 16 bold")
b1.pack(side=LEFT, padx=5, pady=5)
b1.bind("<Button-1>", click)

b2 = Button(f1, text="0", padx=10, pady=10, font="Times 20 bold")
b2.pack(side=LEFT, padx=5, pady=5)
b2.bind("<Button-1>", click)

b3 = Button(f1, text="/", padx=10, pady=10, font="Times 20 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)


b3 = Button(f1, text="00", padx=10, pady=18, font="Times 15 bold")
b3.pack(side=LEFT, padx=5, pady=5)
b3.bind("<Button-1>", click)



f1.pack()

root.mainloop()
