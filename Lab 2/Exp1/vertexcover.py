from graph import is_vertex_cover
from random import randint

def approx1(G):
    C = set()
    degrees = []
    nodes = []
    G2 = G.copy()
    for node in G.adj:
        nodes.append(node)
        degree = len(G.adjacent_nodes(node))
        degrees.append(degree)
    while is_vertex_cover(G2, C) == False:
        v = max(degrees)
        i = degrees.index(v)
        max_node = nodes[i]
        C.add(max_node)
        del max_node
        G2.adjacent_nodes(max_node).clear()
        nodes.adj[i].clear()
        del degrees[i]
    return C

def approx2(G):
    C = set()
    nodes = []
    for node in G.adj:
        nodes.append(node)
    while is_vertex_cover(G, C) == False:
        rand_node = randint(0, len(nodes) - 1)
        C.add(nodes[rand_node])
        del nodes[rand_node]
    return C


def approx3(G):
    C = set()
    edges = []
    G2 = G.copy()

    for FirstNode in G2.adj:
        for SecNode in G2.adj[FirstNode]:
            edges.append([FirstNode, SecNode])

            if [SecNode, FirstNode] in edges and [FirstNode, SecNode] in edges:
                edges.remove([SecNode, FirstNode])


    while not is_vertex_cover(G2, C):
        rand_edge = edges[randint(0, len(edges) - 1)]
        C.add(rand_edge[0])
        C.add(rand_edge[1])

        # how to remove edges
        for incident_edges in G2.adj[rand_edge[0]]:
            G2.adj[rand_edge[0]].remove(incident_edges)

        for incident_edges in G2.adj[rand_edge[1]]:
            G2.adj[rand_edge[1]].remove(incident_edges)

    return C
