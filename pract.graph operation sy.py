class Graph:
    # Constructor to initialize the adjacency matrix with 0s
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # Function to print the adjacency matrix of the graph
    def printGraph(self):
        print("\nAdjacency Matrix:")
        for i in range(self.V):
            for j in range(self.V):
                print(self.graph[i][j], end=" ")
            print()  # New line for each row

    # Function to add an edge between vertices v and w (undirected graph)
    def addEdge(self, v, w):
        print("Adding an edge between", v, "and", w)
        self.graph[v][w] = 1
        self.graph[w][v] = 1

    # Function to remove an edge between vertices v and w
    def removeEdge(self, v, w):
        print("Removing an edge between", v, "and", w)
        self.graph[v][w] = 0
        self.graph[w][v] = 0

    # Function to remove a vertex from the graph (along with its edges)
    def removeVertex(self, v):
        print("Removing vertex", v)
        # Remove the corresponding row
        self.graph.pop(v)
        self.V -= 1  # Update the number of vertices

        # Remove the corresponding column from each remaining row
        for i in range(self.V):
            self.graph[i].pop(v)

    # Function to add a vertex to the graph
    def addVertex(self):
        print("Adding a new vertex")
        self.V += 1
        # Add a 0 for the new vertex in each existing row
        for i in range(self.V - 1):
            self.graph[i].append(0)
        # Append a new row for the new vertex
        self.graph.append([0 for column in range(self.V)])

# Driver code
if __name__ == "__main__":
    # Initialize the graph with 5 vertices
    g = Graph(5)

    # Adding edges between vertices
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)

    # Print the initial adjacency matrix
    g.printGraph()

    # Remove an edge between vertices 0 and 1
    g.removeEdge(0, 1)
    g.printGraph()  # Print the matrix after removing the edge

    # Remove a vert
