from graph import *

def BFS3(G, first_node):
    Q = deque(first_node)
    marked = ()
    predecessor = {}

    while len(Q) != 0:
        current_node = Q.popleft()
        if current_node not in marked:
            marked.update(current_node)
            for node in G.adj[first_node]:
                if node not in marked:
                    Q.append(node)
                    predecessor[node] = current_node

    return predecessor

