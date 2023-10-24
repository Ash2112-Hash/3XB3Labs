import graph
import random

def approx1(G):
    C = set()
    degrees = []
    nodes = []
    G2 = G.copy()
    for node in G.adj:
        nodes.append(node)
        degree = len(adjacent_nodes(node))
        degrees.append(degree)
    while graph.is_vertex_cover(G2, C) == False:
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
    C = {}
    nodes = []
    for node in G:
        nodes.append(node)
    while graph.is_vertex_cover(G, C) == False:
        rand_node = random.randint(0, len(nodes))
        C.append(nodes[rand_node])
        del nodes[rand_node]
    return C

def approx3(G):
    C = {}
    edges = []
    #get list of all the edges in G 
    while graph.is_vertex_cover(G, C) == False:
        rand_edge = random.randint(0, len(edges))
        C.append(edges[rand_edge])
        del edges[rand_edge]
    return C
