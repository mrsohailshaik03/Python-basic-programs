

from sys import maxsize
from itertools import permutations

V = 5

# Implementation of Traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # Store all vertices apart from the source vertex
    vertex = [i for i in range(V) if i != s]
    
    # Store minimum weight Hamiltonian Cycle
    min_path = maxsize
    
    # Generate all permutations of the vertices
    for i in permutations(vertex):
        # Store current path weight (cost)
        current_pathweight = 0
        
        # Compute the current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]  # Returning to the starting point
        
        # Update minimum
        min_path = min(min_path, current_pathweight)
    
    return min_path

# Driver Code
if __name__ == "__main__":
    # Matrix representation of the graph
    graph = [
        [0, 12, 10, 19, 8],
        [12, 0, 3, 7, 2],
        [10, 3, 0, 6, 20],
        [19, 7, 6, 0, 4],
        [8, 2, 20, 4, 0]
    ]
    s = 0  # Starting vertex
    print(travellingSalesmanProblem(graph, s))








