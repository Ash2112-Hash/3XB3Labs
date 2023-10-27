from graph import *

""""""
def is_independent_set(G, S):
    for start in G.adj:
        for end in G.adj[start]:
            if not (start in S or end in S):
                return False
    return True
""""""

def MIS(G):
    nodes = [i for i in range(G.number_of_nodes())]
    new_set = power_set(nodes)
    indpt_set = ()

    if G.number_of_nodes == 0:
        return ()
    if G.number_of_nodes == 1:
        return (G)

    for set in new_set:
        print("it is: ",is_independent_set(G, set))
        if is_independent_set(G, set):
            if len(set) > len(indpt_set):
                indpt_set = set
    return indpt_set

G2 = create_random_graph(10, 20)
print(MIS(G2))
print(MVC(G2))