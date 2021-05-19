from tkinter import *

def upload():
    statusvar.set("Wait Loading.....")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")

root = Tk()

root.geometry("400x400")
root.title("Status bar")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=GROOVE, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Update", command=upload).pack()

root.mainloop()