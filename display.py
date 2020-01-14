try:
    from tkinter import *
except:
    from Tkinter import *


class Display:
    def __init__(self, master, width, height, r, c):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.grid(row = r, column = c)
        self.width = width
        self.height = height
        self.canvas = Canvas(self.frame, width = self.width, height = self.height, bg = "yellow")
        self.canvas.pack()
