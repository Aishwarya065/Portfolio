from sys import maxsize
from itertools import permutations

# Number of vertices in the graph
V = 4

# Implementation of the Traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # Store all vertices apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # Store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)

    # Generate permutations and calculate path weight
    for i in next_permutation:
        # Store current path weight
        current_pathweight = 0

        # Calculate the weight of the current path
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # Update the minimum path weight
        min_path = min(min_path, current_pathweight)

    return min_path

# Driver Code
if __name__ == "__main__":
    # Matrix representation of the graph
    graph = [[0, 10, 15, 20], 
             [10, 0, 35, 25],
             [15, 35, 0, 30], 
             [20, 25, 30, 0]]

    # Starting vertex
    s = 0
    print("The minimum path cost is:", travellingSalesmanProblem(graph, s))
