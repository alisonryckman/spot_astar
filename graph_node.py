class GraphNode():
    def __init__(self, theta, x, y):
        self.x = x
        self.y = y
        self.theta = theta
        self.visited = False
        self.parent = None


    def isVisited(self):
        return self.visited
    
    def setVisited(self):
        self.visited = True

    def setParent(self, parent):
        self.parent = parent