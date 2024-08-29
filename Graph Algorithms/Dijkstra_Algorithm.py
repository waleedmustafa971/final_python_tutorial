# Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative weights. It uses a greedy approach by always selecting the vertex with the smallest known distance.

# Dijkstra's Algorithm Steps:
# Initialize distances from the source to all vertices as infinity, except the source itself (distance is 0).
# Use a priority queue to explore the vertex with the smallest tentative distance.
# Update the distance of neighboring vertices and repeat until all vertices are processed.
# Python Implementation Using heapq:

import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, vertex)
    pq = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Process the current vertex
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Update the shortest distance if found a better path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print("Shortest paths from A:", dijkstra(graph, 'A'))
