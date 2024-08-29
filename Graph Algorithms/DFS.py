# Depth-First Search (DFS)
# DFS is another graph traversal algorithm that explores as far as possible along each branch before backtracking. DFS is useful in scenarios like topological sorting, cycle detection, and pathfinding in mazes.

# DFS Algorithm:
# Start from a given source node.
# Mark the node as visited and recursively explore each unvisited neighbor.
# Backtrack when no more neighbors are unvisited.
# Python Implementation:

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        # Recur for all the vertices adjacent to this vertex
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

visited = set()
print("DFS Traversal starting from vertex 2:")
dfs(graph, 2, visited)
