import numpy as np
from graph import Graph
from matplotlib import pyplot as plt

def main():
    print("hello world")
    graph = Graph()
    # Goal pose tuple in SE2 (different order): (angle, x, y)
    goal_pose = (np.pi/4, 1.2, 0.4)
    # TODO: You are packing then unpacking this tuple. Is there a more efficient way to
    #       provide astar with a goal pose?
    graph.run_a_star(goal_pose)
    
if __name__ == "__main__":
    main()
