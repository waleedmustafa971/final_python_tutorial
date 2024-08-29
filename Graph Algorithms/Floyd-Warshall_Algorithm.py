# This algorithm finds the shortest paths between all pairs of nodes in a graph.

def floyd_warshall(graph):
    # Initialize the distance matrix
    dist = {i: {j: float('inf') for j in graph} for i in graph}
    
    for i in graph:
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j] = graph[i][j]
    
    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist
