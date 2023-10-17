from graph import *

def DFS3(G, first_node):
    S = [first_node]
    marked = set()
    predecessor = {}

    while len(S) != 0:
        current_node = S.pop()
        if current_node not in marked:
            marked.add(current_node)
            for node in G.adj[first_node]:
                if node not in marked:
                    S.append(node)
                    predecessor[node] = current_node

    return predecessor

