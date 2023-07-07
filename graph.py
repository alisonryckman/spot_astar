import numpy as np
from graph_node import GraphNode
from queue import PriorityQueue
from math import floor, ceil


# TODO: Bring these global vars into the main a_star.py file. The goal location is dependent on these values
#       but is provided in main.
XDIM = 20
YDIM = 20
ANGLE_INCREMENTS = 8
RESOLUTION = 0.5
START_X = 0.0
START_Y = 0.0
START_ANGLE = 0.0

class Graph():
    '''
    Graph object that holds the nodes to be visited by Conq in A*
    '''

    def __init__(self):
        '''
        TODO: Should we assume Spot always starts at 0,0?
        goal: tuple containing goal location of spot: (theta, x, y)
        '''

        self.cols = XDIM / RESOLUTION
        self.rows = YDIM / RESOLUTION
        self.angle_dim = ANGLE_INCREMENTS

        self.graph = np.empty([self.angle_dim, self.cols, self.rows], dtype=GraphNode)

        # Priority queue that contains the indices of GraphNodes
        self.queue = PriorityQueue()

        # Construct a new graph with all nodes unvisited
        for a in (range(self.angle_dim)):
            for i in (range(self.cols)):
                for j in (range(self.rows)):
                    th = a * ((2 * np.pi) / self.angle_dim)
                    x = - XDIM / 2 + i * RESOLUTION + RESOLUTION / 2
                    y = YDIM / 2 - j * RESOLUTION - RESOLUTION / 2
                    self.graph[a, i, j] = GraphNode(th, x, y)

    def get_node_index_from_coords(self, xcoord, ycoord, angle):
        '''
        Returns the node in the graph corresponding to the provided Euclidean x, y, theta
        '''
        node_i = floor(xcoord / RESOLUTION) + self.cols / 2
        node_j = self.rows / 2 - ceil(ycoord / RESOLUTION)
        node_a = floor((angle[0] % (2 * np.pi)) / (2 * np.pi / ANGLE_INCREMENTS))
        return (node_a, node_i, node_j)
    

    def get_node_visited(self, index):
        '''
        Returns whether the node at the index is visited 
        '''
        return self.graph[index[0], index[1], index[2]].isVisited()
    
    def set_node_visited(self, index):
        '''
        Sets the node at the index as visited 
        '''
        self.graph[index[0], index[1], index[2]].setVisited()

    def set_node_visited(self, index):
        '''
        Sets the parent of the node at index 
        '''
        self.graph[index[0], index[1], index[2]].setVisited()

    def run_a_star(self, goal_pose):
        start_node_i = self.get_node_index_from_coords(START_X, START_Y, START_ANGLE)
        goal_node_i = self.get_node_index_from_coords(goal_pose(0), goal_pose(1), goal_pose(2))
        # start node has a cost of zero
        self.queue.put((0,start_node_i))
        while not self.queue.empty() & current_node_i != goal_node_i:
            current_node_i = self.queue.get()[1]
            self.set_node_visited(current_node_i)
            neighbor_index_arr = []
            # Check East
            right_node_i = current_node_i
            right_node_
            if current_node_
            

    def compute_f(self, goal):
        self.

    def get_heuristic(self, node1, node)

    def display_graph(self):
        
    def get_neighbors(self):
        # theta, x, y, cost
        neighbors = [[0, 1, 0],
                     [0, 0, 1],
                     [0, -1, 0],
                     [0, 0, -1],
                     [1, 0, 0],
                     [-1, 0, 0]]
        return neighbors