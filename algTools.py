try:
    from tkinter import *
except:
    from Tkinter import *

class AlgTools:
    def __init__(self, master, r, c):

        self.master = master
        self.frame = Frame(self.master)
        self.frame.grid(row = r, column = c)
        self.title = Label(self.frame, text = "Algorithm Control Tools")
        self.title.grid(row = 0, column = 0)
        self.buttons = {
            "Start": Button(self.frame, text = "Start"),
            "Run": Button(self.frame, text = "Run"),
            "Stop": Button(self.frame, text = "Stop"),
            "Step": Button(self.frame,text = "Step")
        }
        for i,button in enumerate(self.buttons):
            self.buttons[button].grid(row = i + 1, column = 0)
