from tkinter import *
import pygame
from tkinter import filedialog


root = Tk()

root.configure(background='black')


def add():
    song = filedialog.askopenfilename(initialdir='tkinter music/', title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ))

    song = song.replace("C:/Users/Tenac/Music/tkinter music/", "")
    song = song.replace(".mp3", "")

    list1.insert(END, song)


def play_it():
    song = list1.get(ACTIVE)
    song = f'C:/Users/Tenac/Music/tkinter music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stop_it():
    pygame.mixer.music.stop()
    list1.selection_clear(ACTIVE)

root.geometry("800x450")
root.title("Music player")
#root.iconbitmap("2.svg")

pygame.mixer.init()

list1 = Listbox(root, bg="Light blue", fg="white", width=80, selectbackground="white", selectforeground="light blue")
list1.pack(pady=30)
list1.insert(END, "SONGS.........")

play_btn = PhotoImage(file="play1.png")
stop_btn = PhotoImage(file="stop2.png")
forward_btn = PhotoImage(file="forward1.png")
back_btn = PhotoImage(file="back2.png")

btns_frame = Frame(root)
btns_frame.pack()

b1 = Button(btns_frame, image=play_btn, borderwidth=0, command=play_it)
b2 = Button(btns_frame, image=back_btn, borderwidth=0, command=None)
b3 = Button(btns_frame, image=forward_btn, borderwidth=0, command=None)
b4 = Button(btns_frame, image=stop_btn, borderwidth=0, command=stop_it)

b1.grid(row=0, column=4)
b2.grid(row=0, column=3)
b3.grid(row=0, column=6)
b4.grid(row=0, column=5)

menubar = Menu(root)
song = Menu(menubar, tearoff=0)
song.add_command(label="add new song", command=add)
menubar.add_cascade(label="Add", menu=song)
root.config(menu=menubar)
root.mainloop()
