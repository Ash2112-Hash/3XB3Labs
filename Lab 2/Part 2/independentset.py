from graph import *

def is_independent_set(G, S):
    for node1 in S:
        for node2 in S:
            if (node2 in G.adjacent_nodes(node1)):
                return False
    return True

def MIS(G):
    nodes = [i for i in range(G.number_of_nodes())]
    subsets = power_set(nodes)
    max_set = []
    for subset in subsets:
        if is_independent_set(G, subset):
            if len(subset) > len(max_set):
                max_set = subset
    return max_set