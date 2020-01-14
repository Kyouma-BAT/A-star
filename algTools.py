try:
    from tkinter import *
except:
    from Tkinter import *

class AlgTools:
    def __init__(self, master, r, c):

        self.master = master
        self.frame = Frame(self.master)
        self.frame.grid(row = r, column = c, sticky = W)
        self.title = Label(self.frame, text = "Algorithm Control Tools")
        self.title.grid(row = 0, column = 0, sticky = W)
        self.buttonFrame = Frame(self.frame)
        self.buttonFrame.grid(row = 1, column = 0, sticky = W)
        self.buttonSet = ["Start", "Stop", "Step", "Run", "Reset"]
        self.buttonPositions = [(1,0),(2,1),(3,0),(2,0),(1,1)]
        self.buttons = []
        for i,each in enumerate(self.buttonSet):
            self.buttons.append(Button(self.buttonFrame, text = self.buttonSet[i]))
            self.buttons[i].grid(row = self.buttonPositions[i][0], column = self.buttonPositions[i][1], sticky = W)
