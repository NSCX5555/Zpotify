import tkinter as tk
import fnmatch
import os
import sys
import pygame
from pygame import mixer

canvas = tk.Tk()
canvas.title("Zpotify")
ico = tk.PhotoImage(file="Zpotify.png")
canvas.iconphoto(False,ico)
canvas.geometry("700x450")
canvas.configure(bg = 'black')
canvas.resizable(False, False)

rootpath = "C:\\Users\keemo\Desktop\Zpotify\Songs"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file = "prev_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
next_img = tk.PhotoImage(file = "next_img.png")

def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def prev_next():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

listBox = tk.Listbox(canvas, fg = "white", bg = "black", width = 100, font = ('times new roman',14))
listBox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, bg = 'black', fg = 'white', font = ('times new roman', 18))
label.pack(pady = 15)

top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center')

prevButton = tk.Button(canvas, text = "Prev", image = prev_img, bg = 'black', borderwidth = 0, command = prev_next)
prevButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(canvas, text = "Play", image = play_img, bg = 'black', borderwidth = 0, command = select)
playButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(canvas, text = "Next", image = next_img, bg = 'black', borderwidth = 0, command = play_next)
nextButton.pack(pady = 15, in_ = top, side = 'left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
