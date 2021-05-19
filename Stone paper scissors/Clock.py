from tkinter import *
import time

root = Tk()
root.geometry("450x200")
root.maxsize(450,200)
root.minsize(450,200)
root.title("Tokei")
root.configure(background="black")
root.wm_iconbitmap("icons8-clock.svg")

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    time_zone = time.strftime("%Z")

    label1.config(text = hour + ":" + minute + ":" + second + " " + am_pm)
    label1.after(1000, clock)
    label2.config(text= time_zone + " :: " + day)


def update():
    label1.config(text="New Text")

label1 = Label(root, text="", font=("Lucida", 52), fg="light blue", bg="black")
label1.pack(pady=20)

label2 = Label(root, text="", font=("Times", 22), fg="white", bg="black")
label2.pack(pady=10)

clock()
root.mainloop()