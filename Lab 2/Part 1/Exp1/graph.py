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

    def copy(self):     #returns a copy of the graph object
        copied_G = Graph(self.number_of_nodes())

        for parent_node, adjacent_node in self.adj.items():

            for each_node in adjacent_node:
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

# has_cycle(G) function determines if a graph: G has a cycle within it
#NOTE: in our implementation, has cycle does include self loops within the graph where a cycle is present
def has_cycle(G):

    # a recursive dfs to visit all the paths to see if a cycle exists. If cycle exits, return True, otherwise return false
    def recur_DFS(node, first_node, marked):
        marked.add(node)
        for adjacent_node in G.adj[node]:
            if adjacent_node not in marked:
                if recur_DFS(adjacent_node, node, marked):
                    return True
            else:
                if adjacent_node != first_node:
                    return True
        return False

    # if a graph is empty, return false
    if not G.adj:
        return False


    # iterates through all nodes of the graph and applies the recur_DFS to determine if a cycle exists (markedNodes is used to track visited nodes)
    markedNodes = set()
    for node in G.adj:
        if node not in markedNodes and recur_DFS(node, None, markedNodes):
            return True

    return False


# Is_connected(G) function determines if all node pairs within a graph is connected
def Is_connected(G):

    # if a graph is empty, return false
    if not G.adj:
        return False

    # access the start node of the graph
    start_node = next(iter(G.adj))

    # markedNodes is used to track visited nodes
    markedNodes = set()

    # a recursive dfs to visit all the paths to see if the node pairs are connected
    def recur_DFS(each_node):
        markedNodes.add(each_node)

        for adjacent_node in G.adj[each_node]:
            if adjacent_node not in markedNodes:
                recur_DFS(adjacent_node)

    # start the recursion on first node
    recur_DFS(start_node)

    # return if the length of the markedNodes is equal to the length of graph's adjacency list (ie. all node pair paths have been detected if they are all connected)
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
        if (a != b) or (b not in rand_graph.adj[a]):
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


G = Graph(0)
G.add_node()
G.add_node()
G.add_node()
G.add_node()
G.add_node()
G.add_node()
G.add_edge(0, 1)
G.add_edge(0, 0)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
"""
