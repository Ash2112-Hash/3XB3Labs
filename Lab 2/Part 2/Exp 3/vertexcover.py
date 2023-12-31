import random

from graph import *
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
    while not is_vertex_cover(G, C) and len(degrees) != 0:
        v = max(degrees)
        i = degrees.index(v)
        max_node = nodes[i]
        C.add(max_node)
        edges = G2.adjacent_nodes(max_node)
        del edges
        del nodes[i]
        del degrees[i]
    return C


def approx2(G):
    C = set()
    G2 = G.copy()
    nodes = list(G2.adj.keys())

    while not is_vertex_cover(G, C):
        if nodes:
            v = random.choice(nodes)

            if v not in C:
                C.add(v)

            else:
                continue
    return C


def approx3(G):
    C = set()
    G2 = G.copy()
    # print(G2.adj == G.adj)

    while not is_vertex_cover(G, C):


        u = random.choice(list(G2.adj.keys()))

        if G2.adj[u]:  # TODO add check to other approx functions
            v = random.choice(G2.adj[u])

        else:
            continue

        #print(u, v)
        #print(G2.adj)
        # print(G2.adj[u])
        # print(G2.adj[v])
        C.add(u)
        C.add(v)

        for node in G2.adj[u]:
            if node != v and node != u:
                G2.adj[u].remove(node)
                G2.adj[node].remove(u)

        for node in G2.adj[v]:
            if node != v and node != u:
                G2.adj[v].remove(node)
                G2.adj[node].remove(v)

        #print(G2.adj)

    return C

