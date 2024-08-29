# Dijkstra's Algorithm
# Dijkstra's algorithm is used to find the shortest path from a single source to all other nodes in a weighted graph with non-negative weights.

import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity and set start node to 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # Priority queue with (distance, node)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example graph as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

print(dijkstra(graph, 'A'))  # Shortest path from A
