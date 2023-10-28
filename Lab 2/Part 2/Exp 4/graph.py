from collections import deque
from random import randint


# Undirected graph using an adjacency list
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

    def copy(self):     #TODO confirm with TA if need to be moved
        copied_G = Graph(self.number_of_nodes())

        for parent_node, incident_node in self.adj.items():

            for each_node in incident_node:
                copied_G.add_edge(parent_node, each_node)

        return copied_G


# Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1: True}
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


def BFS2(G, node1, node2):  # TODO need to test
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


# Depth First Search
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


def DFS2(G, node1, node2):
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
    def recur_DFS(node, first_node, marked):  # a recursive dfs to visit all the paths to see if a cycle exists
        marked.add(node)
        for incident_node in G.adj[node]:
            if incident_node not in marked:
                if recur_DFS(incident_node, node, marked):
                    return True
            else:
                if incident_node != first_node:
                    return True
        return False

    markedNodes = set()
    for node in G.adj:
        if node not in markedNodes and recur_DFS(node, None, markedNodes):
            return True

    return False


def Is_connected(G):
    if not G.adj:
        return False

    start_node = next(iter(G.adj))
    markedNodes = set()

    def recur_DFS(each_node):
        markedNodes.add(each_node)

        for incident_node in G.adj[each_node]:
            if incident_node not in markedNodes:
                recur_DFS(incident_node)

    recur_DFS(start_node)

    return len(markedNodes) == len(G.adj)


# Use the methods below to determine minimum Vertex Covers
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
            if not (start in C or end in C):
                return False
    return True


def MVC(G):
    nodes = [i for i in range(G.number_of_nodes())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


def create_random_graph(i, j):
    rand_graph = Graph(i)

    # maximum number of unrepeating edges in undirected graph
    max_edge = (i * (i - 1) / 2)
    if j > max_edge:
        j = max_edge

    while j > 0:
        a = randint(0, i - 1)
        b = randint(0, i - 1)
        if (a != b) and (b not in rand_graph.adj[a]) and (a not in rand_graph.adj[b]):
            rand_graph.add_edge(a, b)
            j -= 1  # decrease j to continue loop and randomization process until no edges are left

    return rand_graph


### TODO TESTING REMOVE LATER #######################################
"""
rand_G = create_random_graph(5, 10)
print(rand_G.number_of_nodes())
print(rand_G.adj)
print(has_cycle(rand_G))
print(Is_connected(rand_G))


G = Graph(10000)
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
print(has_cycle(G))
print(Is_connected(G))
"""

G = Graph(0)
G.add_node()
G.add_node()
G.add_node()
G.add_node()
G.add_node()
G.add_node()
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(4, 5)

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