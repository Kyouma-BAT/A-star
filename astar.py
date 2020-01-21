from constants import *
from field import *
import math



class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.prevNode = None
        self.state = None
        self.adjacent = [(x+1,y),(x-1,y), (x,y+1), (x, y-1)]
        self.h_cost = 0
        self.g_cost = 0
        self.f_cost = 0
        self.traversable = True
        self.start = False
        self.end = False

    def g_calc(self):
        self.g_cost = self.prevNode.g_cost + 1

    def set_end(self):
        self.end = True

    def set_start(self):
        self.start = True

    def is_traversable(self):
        return self.traversable

    def notTraversable(self):
        self.traversable = False

    def getCoords(self):
        return self.x, self.y


    def open(self):
        self.state = open

    def close(self):
        self.state = closed


class Astar:
    def __init__(self, field):
        self.f = field
        self.start = None
        self.end = None
        self.nodes = [[Node(j,i) for j in range(COLUMNS)]for i in range(ROWS)]
        self.open = []
        self.closed = []


    def init_map(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.f.getNode(j,i) == "wall":
                    self.nodes[j][i].notTraversable()
                if self.f.getNode(j,i) == "start":
                    self.start = (j,i)
                    self.nodes[i][j].set_start()
                    self.open.append(self.nodes[i][j])
                if self.f.getNode(i,j) == "end":
                    self.end = (j,i)
                    self.nodes[i][j].set_end()


    def g_cost(self,node):
        node.g_cost = node.prevNode.g_cost + 1

        return

    def h_cost(self, node):
        x,y = node.getCoords()
        node.h_cost = math.sqrt((self.end[0] - x)**2 + (self.end[1] - y)**2)
        return node.h_cost



    def f_cost(self, node):
        node.f_cost = node.g_cost + node.h_cost
        return node.g_cost + node.h_cost

if __name__ == "__main__":
    f = Field()
    f.setNode("end", 1,2)
    f.setNode("start", 0,0)
    f.setNode("wall", 1,1)

    
    a = Astar(f)
    a.init_map()
    print(a.start)
    print(a.end)
    print(a.nodes[1][0].is_traversable())
