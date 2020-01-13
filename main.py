try:
    from tkinter import *
except:
    from Tkinter import *
from constants import *
from algTools import *


if __name__ == "__main__":
    root = Tk()
    root.title("A*")
    toolsFrame = Frame(root)
    toolsFrame.grid(row = 0, column = 0, sticky = N)

    algTools = AlgTools(toolsFrame, 0,0)


    drawToolsFrame = Frame(toolsFrame, bg = "blue", height = 100, width = 100)
    drawToolsFrame.grid(row = 1, column = 0, pady = 100)

    canva = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")
    canva.grid(row = 0, column = 1)


    root.mainloop()
