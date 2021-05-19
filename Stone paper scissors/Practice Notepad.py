from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    Textbox.delete(1.0, END)

def newwindow():
    status.set("Wait Loading.....")
    sbar.update()
    import time
    time.sleep(2)
    status.set("Sorry the function is not ready")

def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(Textbox.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(Textbox.get(1.0, END))
        f.close()


def saveas():
    status.set("Wait Loading.....")
    sbar.update()
    import time
    time.sleep(2)
    status.set("Sorry the function is not ready")

def printo():
    status.set("Wait Loading.....")
    sbar.update()
    import time
    time.sleep(2)
    status.set("Sorry the function is not ready")

def open():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        Textbox.delete(1.0, END)
        f = open(file, "r")
        Textbox.insert(1.0, f.read())
        f.close()

def exit():
    root.destroy()

def cut():
    Textbox.event_generate(("<>"))

def copy():
    Textbox.event_generate(("<>"))

def paste():
    Textbox.event_generate(("<>"))

def delete():
    Textbox.event_generate(("<>"))

def undo():
    status.set("Wait Loading.....")
    sbar.update()
    import time
    time.sleep(2)
    status.set("Sorry the function is not ready")

def redo():
    status.set("Wait Loading.....")
    sbar.update()
    import time
    time.sleep(2)
    status.set("Sorry the function is not ready")

def zoom():
    status.set("Wait Loading.....")
    sbar.update()
    import time
    time.sleep(2)
    status.set("Sorry the function is not ready")

def format():
    status.set("Wait Loading.....")
    sbar.update()
    import time
    time.sleep(2)
    status.set("You can write....")

def help():
    showinfo("help","You can find more help by clicking this link www.practicenotepad.info")

def about():
    showinfo("Practice Notepad", "By Mr.Nair")


root = Tk()
root.geometry("400x400")
#root.wm_iconbitmap("1.ico")
root.title("Practice Notepad")


status = StringVar()
status.set("You can write....")
sbar = Label(root, textvariable=status, relief=RIDGE, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

Textbox = Text(root, font="times 22  italic")
file = None
Textbox.pack(expand=True, fill=BOTH)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New                                   ctrl+N", command=newfile)
filemenu.add_command(label="New window          ctrl+shift+N", command=newwindow)
filemenu.add_command(label="Save                                  ctrl+S", command=save)
filemenu.add_command(label="Save as                   ctrl+shift+S", command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Print                                 ctrl+P", command=printo)
filemenu.add_command(label="Open                                ctrl+O", command=open)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo             ctrl+Z", command=undo)
editmenu.add_command(label="Redo             ctrl+shift+Z", command=redo)
editmenu.add_separator()
editmenu.add_command(label="Copy             ctrl+C", command=copy)
editmenu.add_command(label="Cut              ctrl+X", command=cut)
editmenu.add_command(label="Paste            ctrl+V", command=paste)
editmenu.add_command(label="Delete", command=delete)
menubar.add_cascade(label="Edit", menu=editmenu)

viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label = "Zoom >", command=zoom)
viewmenu.add_command(label = "Format", command=format)
menubar.add_cascade(label="View", menu=viewmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Help", command=help)
helpmenu.add_command(label = "About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

scroll = Scrollbar(Textbox)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=Textbox.yview)
Textbox.config(yscrollcommand=scroll.set)


root.mainloop()