import matplotlib.pyplot as plt
import numpy as np
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

X = ['5 Nodes', '10 Nodes', '15 Nodes', '20 Nodes']

G1 = create_random_graph(5,10)
print(G1.adj)
print(MIS(G1))
print(MVC(G1))
G2 = create_random_graph(10,20)
print(G2.adj)
print(MIS(G2))
print(MVC(G2))
G3 = create_random_graph(15,30)
print(G3.adj)
print(MIS(G3))
print(MVC(G3))
G4 = create_random_graph(20,40)
print(G4.adj)
print(MIS(G4))
print(MVC(G4))

max_idpt_set = [len(MIS(G1)), len(MIS(G2)), len(MIS(G3)), len(MIS(G4))]
min_ver_cov = [len(MVC(G1)), len(MVC(G2)), len(MVC(G3)), len(MVC(G4))]
total_nodes = [G1.number_of_nodes(), G2.number_of_nodes(), G3.number_of_nodes(), G4.number_of_nodes()]
  
X_axis = np.arange(len(X)) 

plt.bar(X_axis - 0.3, max_idpt_set, 0.2, label = 'MIS(G)') 
plt.bar(X_axis - 0.1, min_ver_cov, 0.2, label = 'MVC(G)') 
plt.bar(X_axis + 0.1, total_nodes, 0.2, label = 'Total Nodes in G') 
  
plt.xticks(X_axis, X) 
plt.xlabel("Randomized Graphs (G)") 
plt.ylabel("Number of Nodes") 
plt.title("Relationship Between MIS(G), MVC(G) and Total Nodes") 
plt.legend() 
plt.show() 