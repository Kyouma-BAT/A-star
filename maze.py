import random
from constants import *
import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = "wall"
        self.neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if self.x == 0:
            self.neighbours.remove((x - 1, y))
        if self.y == 0:
            self.neighbours.remove((x, y - 1))
        if self.x == COLUMNS - 1:
            self.neighbours.remove((x + 1, y))
        if self.y == ROWS - 1:
            self.neighbours.remove((x, y + 1))



class Maze:
    def __init__(self, field):
        self.f = field
        self.maze = [[Point(j,i) for j in range(COLUMNS)]for i in range(ROWS)]
        self.walls = []
        self.update = None

    def step(self, point):
        if self.is_traversable(point):
            point.type = "path"
            self.f.setNode("empty", point.x, point.y)
            for each in point.neighbours:
                node = self.get_node(each[0],each[1])
                if (node.type != "path") and (self.is_traversable(node)):
                    self.walls.append(node)
        else:
            return

    def generate_maze(self):
        self.maze = [[Point(j,i) for j in range(COLUMNS)]for i in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.get_node(j,i).type == "wall":
                    self.f.setNode("wall", j,i)
        self.update()
        self.walls = []
        node = self.get_node(25,25)
        self.step(node)
        k = 0
        while(len(self.walls) > 0):
            k += 1
            node = random.choice(self.walls)
            self.step(node)
            self.walls.remove(node)
            if k % 40 == 0:
                self.update()

    def setUpdateFunction(self, function):
        self.update = function

    def get_node(self,x,y):
        if x < 0 or y < 0 or x >= COLUMNS or y >= ROWS:
            return Point(-1,-1)
        else:
            return self.maze[y][x]

    def is_traversable(self,point):
        ret = True
        k = 0
        grid =[]
        startX = point.x-1
        startY = point.y-1

        for i in range(3):
            for j in range(3):
                grid.append(self.get_node(startX + j, startY + i))
        if ((grid[0].type == "path")and(grid[1].type == "path")and(grid[3].type == "path"))or((grid[1].type == "path")and(grid[2].type == "path")and(grid[5].type == "path"))or((grid[3].type == "path")and(grid[6].type == "path")and(grid[7].type == "path"))or((grid[7].type == "path")and(grid[8].type == "path")and(grid[5].type == "path")):
            ret = False
        for each in point.neighbours:
            if self.get_node(each[0], each[1]).type == "path":
                k += 1
        if k >= 2:
            ret = False


        return ret
