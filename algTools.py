try:
    from tkinter import *
except:
    from Tkinter import *

class AlgTools:
    def __init__(self, master, r, c, bg = "black", fg = "white"):
        self.bg = bg
        self.fg = fg
        self.state = DISABLED

        self.master = master
        self.frame = Frame(self.master, bg = self.bg)
        self.frame.grid(row = r, column = c, sticky = W)
        self.title = Label(self.frame, text = "Algorithm Control Tools: ", bg = self.bg, fg = self.fg)
        self.title.grid(row = 0, column = 0, sticky = W)
        self.buttonFrame = Frame(self.frame, bg = self.bg)
        self.buttonFrame.grid(row = 1, column = 0, sticky = W)
        self.buttonSet = ["Start", "Stop", "Step", "Run", "Reset"]
        self.buttonPositions = [(1,0),(2,1),(3,0),(2,0),(1,1)]
        self.buttons = []
        for i,each in enumerate(self.buttonSet):
            self.buttons.append(Button(self.buttonFrame, text = self.buttonSet[i], bg = self.bg, fg = self.fg, borderwidth = 0, state = self.state))
            self.buttons[i].grid(row = self.buttonPositions[i][0], column = self.buttonPositions[i][1], sticky = W)
            
    def flipState(self):
        if self.state == NORMAL:
            self.state = DISABLED
        else:
            self.state = NORMAL
        for each in self.buttons:
            each.configure(state = self.state)
