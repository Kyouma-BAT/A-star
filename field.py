from constants import *

class Field:
    def __init__(self):
        self.grid = [["empty" for i in range(COLUMNS)] for i in range(ROWS)]
        self.activeTool = "wall"
        self.colorMap = {
            "empty": "white",
            "wall": "black",
            "start": "green",
            "end": "red",
            "open": "yellow",
            "closed": "brown",
            "path": "blue"
        }

    def findStart(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.grid[i][j] == "start":
                    return (j,i)

    def findEnd(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.grid[i][j] == "end":
                    return (j,i)



    def setTool(self, tool):
        self.activeTool = tool

    def getTool(self):
        return self.activeTool

    def setNode(self,node,x,y):
        self.grid[y][x] = node

    def getNode(self,x,y):
        return self.grid[y][x]
