# A strongly connected component (SCC) in a directed graph is a maximal subgraph where every vertex is reachable from every other vertex. Kosaraju's Algorithm is commonly used to find SCCs.

def kosaraju_scc(graph):
    visited = set()
    stack = []
    
    def fill_order(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                fill_order(neighbor)
        stack.append(node)
    
    def dfs(node, transposed_graph, component):
        visited.add(node)
        component.append(node)
        for neighbor in transposed_graph[node]:
            if neighbor not in visited:
                dfs(neighbor, transposed_graph, component)
    
    for node in graph:
        if node not in visited:
            fill_order(node)
    
    transposed_graph = {node: [] for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            transposed_graph[neighbor].append(node)
    
    visited.clear()
    sccs = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs(node, transposed_graph, component)
            sccs.append(component)
    
    return sccs
