from collections import deque
from random import randint

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes(self):
        return len(self.adj)


#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

def BFS2(G, node1, node2):      #TODO need to test
    path = []
    Q = deque([(node1, [node1])])
    marked = {node: False for node in G.adj}

    while len(Q) != 0:
        current_node, path = Q.popleft()
        marked[current_node] = True

        for neighbour in G.adj[current_node]:
            if neighbour == node2:
                path.append(node2)
                return path
            if not marked[neighbour]:
                Q.append((neighbour, path + [neighbour]))
                marked[neighbour] = True

    return []

def BFS3(G, first_node):
    Q = deque(first_node)
    marked = set()
    predecessor = {}

    while len(Q) != 0:
        current_node = Q.popleft()
        if current_node not in marked:
            marked.add(current_node)
            for node in G.adj[first_node]:
                if node not in marked:
                    Q.append(node)
                    predecessor[node] = current_node

    return predecessor

#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

def DFS2(G, node1, node2):  #TODO need to test
    path = []
    S = [(node1, [node1])]
    marked = {node: False for node in G.adj}

    while len(S) != 0:
        current_node, path = S.pop()
        marked[current_node] = True

        for neighbour in G.adj[current_node]:
            if neighbour == node2:
                path.append(neighbour)
                return path

            if not marked[neighbour]:
                marked[neighbour] = True
                S.append((neighbour, path + [neighbour]))
    return []

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

def has_cycle(G):

    def decision_DFS3(first_node):  #TODO confirm with TA for this
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
                    else:
                        if predecessor.get(current_node) != node: # implies we reached the current node from another node thats already marked
                            return True

        return False

    if (not G.adj):
        return False

    else:
        for each_node in G.adj:
            if decision_DFS3(each_node):
                return True

    return False



def Is_connected(G):        #TODO confirm if checking all nodes are visited or smth else
    start_node = next(iter(G.adj))
    visited = set()

    for node in G.adj:          #TODO confirm if we can use normal DFS or DFS2
        if node != start_node:
            path = DFS2(G, start_node, node)

            for each_node in path:
                visited.add(each_node)

            #print(start_node, node, path, visited)

    return G.adj.keys() == visited


### TESTING TODO REMOVE LATER ###
G = Graph(0)
G.add_node()
G.add_node()
G.add_node()
G.add_node()
G.add_node()
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
print(has_cycle(G))
print(Is_connected(G))

#Use the methods below to determine minimum Vertex Covers
def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


"""  
#Create random generated graph
def create_random_graph(i, j):
    # maximum number of unrepeating edges in undirected graph
    if j > (i * (i - 1) / 2):
        j = i * (i - 1) / 2
    for _ in range(i):
        adjacency_list.append([])
    for n in j:
        a = randint(0, i - 1)
        b = randint(0, i - 1)
        if ((a == b) or (b in adjacency_list[a])):
            #decrease i to "re-do" the randomization so that it can generate non-repeating edges
            n -= 1
            continue
        add_edge(a, b)
"""