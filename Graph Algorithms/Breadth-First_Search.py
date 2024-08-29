# BFS is an algorithm for traversing or searching graph data structures. It starts at a selected node and explores all its neighboring nodes before moving to the next level of neighbors. BFS is particularly useful in finding the shortest path in an unweighted graph.

# BFS Algorithm:
# Start from a given source node.
# Mark the node as visited and enqueue it.
# While the queue is not empty, dequeue a node, process it, and enqueue all its unvisited neighbors.
# Python Implementation:


from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        # Process neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print("BFS Traversal starting from vertex 2:")
bfs(graph, 2)
