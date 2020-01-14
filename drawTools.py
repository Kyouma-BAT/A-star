try:
    from tkinter import *
except:
    from Tkinter import *


class DrawTools:
    def __init__(self, master, r, c):

        self.choice = IntVar()

        self.master = master
        self.frame = Frame(self.master, pady = 50)
        self.frame.grid(row = r, column = c, sticky = W)
        self.title = Label(self.frame, text = "Drawing Tools")
        self.title.grid(row = 0, column = 0, sticky = W)


        self.checkBoxFrame = Frame(self.frame)
        self.checkBoxFrame.grid(row = 1, column = 0)
        self.options = [
            ("Wall", 0),
            ("Eraser",1),
            ("Start",2),
            ("End",3)
        ]
        self.radioBoxes = []
        for option in self.options:
            self.radioBoxes.append(Radiobutton(self.checkBoxFrame, text = option[0], variable = self.choice, value = option[1], command = self.out))
        for each in self.radioBoxes:
            each.pack()



        self.buttonFrame = Frame(self.frame)
        self.buttonFrame.grid(row = 2, column = 0, sticky = W)
        self.buttonSet = ["Clear", "Save", "Load"]
        self.buttonPositions = [(0,0),(1,0),(1,1)]
        self.buttons = []
        for i,each in enumerate(self.buttonSet):
            self.buttons.append(Button(self.buttonFrame, text = self.buttonSet[i]))
            self.buttons[i].grid(row = self.buttonPositions[i][0], column = self.buttonPositions[i][1], sticky = W)

    def out(self):
        print(self.choice.get())
