import graph
import random

def approx1(G):
    C = set()
    degrees = []
    nodes = []
    for node in G:
        nodes.append(node)
        degree = #number of edges attached to node (this is the part i'm confused about LOL)
        degrees.append(degree)
    while graph.is_vertex_cover(G, C) == False:
        i = degrees.index(max(degrees))
        C.add(nodes[i])
        del nodes[i]
        del degrees[i]
    return C

def approx2(G):
    C = set()
    nodes = []
    for node in G.adj:
        nodes.append(node)
    while graph.is_vertex_cover(G, C) == False:
        rand_node = random.randint(0, len(nodes) - 1)
        C.add(nodes[rand_node])
        del nodes[rand_node]
    return C

def approx3(G):
    C = set()
    edges = []
    #get list of all the edges in G 
    while graph.is_vertex_cover(G, C) == False:
        rand_edge = random.randint(0, len(edges))
        C.add(edges[rand_edge])
        del edges[rand_edge]
    return C
