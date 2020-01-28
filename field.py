from constants import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.traversable = True
        self.travelled = False
        self.neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if self.x == 0:
            self.neighbours.remove((x - 1, y))
        if self.y == 0:
            self.neighbours.remove((x, y - 1))
        if self.x == COLUMNS - 1:
            self.neighbours.remove((x + 1, y))
        if self.y == ROWS - 1:
            self.neighbours.remove((x, y + 1))



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
        self.points = [[Point(j,i) for j in range(COLUMNS)]for i in range(ROWS)]

    def setTool(self, tool):
        self.activeTool = tool

    def getTool(self):
        return self.activeTool

    def setNode(self, node, x, y):
        self.grid[y][x] = node

    def getNode(self, x, y):
        return self.grid[y][x]
