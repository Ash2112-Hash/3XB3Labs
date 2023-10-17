# ******************* Experiment Graph Prep Functions - Continued *******************
# Prep functions associated with the graphs that are needed to create the experiments

from DFS3 import *
from BFS3 import *

class GraphCalcs:

    def has_cycle(self, G):
        #TODO confirm this
        def alt_DFS3(first_node):
            S = [first_node]
            marked = set()
            predecessor = {}

            while len(S) != 0:
                current_node = S.pop()
                if current_node not in marked:
                    marked.add(current_node)

                    for node in G.adj[current_node]:
                        if node not in marked:
                            S.append(node)
                            predecessor[node] = current_node

                        elif predecessor.get(current_node) != node:
                            #implies we reached the current node from another node thats already marked
                            return True
            return False


        for each_node in G.adj:

            if alt_DFS3(each_node):
                return True

        return False


    def Is_connected(self, G):
        pass



