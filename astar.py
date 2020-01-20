class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.prevNode = None
        self.state = None
        self.adjacent = [(x+1,y),(x-1,y), (x,y+1), (x, y-1)]
        self.h_cost = 0
        self.g_cost = 0


    def open(self):
        self.state = open

    def close(self):
        self.state = closed


class Astar:
    def __init__(self, display, field):
        self.f = field
        self.start = self.f.findStart()
        self.end = self.f.findEnd()





    def g_cost(self,node):


        return

    def h_cost(self):


        return



    def f_cost(self, node):
        return self.g_cost(node) + self.h_cost(node)
