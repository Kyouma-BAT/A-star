try:
    from tkinter import *
except:
    from Tkinter import *
from constants import *
from algTools import *
from drawTools import *
from display import *


if __name__ == "__main__":
    root = Tk()
    root.title("A*")
    root.configure(background = BACKGROUND)

    toolsFrame = Frame(root, bg = BACKGROUND)
    toolsFrame.grid(row = 0, column = 0, sticky = N)

    algTools = AlgTools(toolsFrame, 0,0, BACKGROUND)

    drawTools = DrawTools(toolsFrame, 1,0, BACKGROUND)

    display = Display(root, CANVAS_WIDTH, CANVAS_HEIGHT, 0, 1)





    root.mainloop()
