# Graphs can be represented in various ways depending on the problem and the efficiency required. The two most common representations are:

# Adjacency Matrix: A 2D array where each cell represents the presence or absence of an edge between two vertices.
# Adjacency List: A list where each element represents a vertex, and the element contains a list of connected vertices.
# Adjacency Matrix Example:


# Example: Graph with 4 vertices
graph_matrix = [
    [0, 1, 0, 0],  # Vertex 0 connected to Vertex 1
    [1, 0, 1, 1],  # Vertex 1 connected to Vertex 0, 2, and 3
    [0, 1, 0, 1],  # Vertex 2 connected to Vertex 1 and 3
    [0, 1, 1, 0]   # Vertex 3 connected to Vertex 1 and 2
]

# Adjacency List Example:

# Example: Graph with 4 vertices
graph_list = {
    0: [1],        # Vertex 0 connected to Vertex 1
    1: [0, 2, 3],  # Vertex 1 connected to Vertex 0, 2, and 3
    2: [1, 3],     # Vertex 2 connected to Vertex 1 and 3
    3: [1, 2]      # Vertex 3 connected to Vertex 1 and 2
}

