# Kruskal’s algorithm finds the minimum spanning tree by sorting edges by weight and adding them one by one, as long as they don’t form a cycle.

def kruskal(graph):
    parent = {}
    
    def find(node):
        if parent[node] == node:
            return node
        return find(parent[node])
    
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            parent[root2] = root1
    
    mst = []
    edges = sorted(graph['edges'], key=lambda edge: edge[2])
    
    for node in graph['nodes']:
        parent[node] = node
    
    for edge in edges:
        node1, node2, weight = edge
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append(edge)
    
    return mst
