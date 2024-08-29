# # The Ford-Fulkerson method computes the maximum flow in a flow network. It uses depth-first search (DFS) or breadth-first search (BFS) to find augmenting paths and improves the flow iteratively.

# Time Complexity: Depends on the implementation (DFS/BFS).
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for v in range(self.V):
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

                    if v == sink:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
