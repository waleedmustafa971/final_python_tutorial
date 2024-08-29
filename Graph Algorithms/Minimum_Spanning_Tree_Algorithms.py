# Prim's Algorithm
# Prim's algorithm finds a minimum spanning tree for a graph, ensuring that the total weight of the tree is minimized.

def prim(graph, start):
    mst = []  # List to store the Minimum Spanning Tree
    visited = set([start])
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)
    
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            
            for next_to, next_cost in graph[to].items():
                if next_to not in visited:
                    heapq.heappush(edges, (next_cost, to, next_to))
    
    return mst
