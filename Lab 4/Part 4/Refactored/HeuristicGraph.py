from typing import Dict

import WeightedGraph

class HeuristicGraph(WeightedGraph):

    def __init__(self):
        self.adj = {}
        self.weights = {}
        self.heuristic: Dict[int, float] = {}

    def get_adj_nodes(self, node: int) -> [int]:
        return self.adj[node]

    def add_node(self, node: int):
        self.adj[node] = []

    def add_edge(self, start: int, end: int, w: float):
        if end not in self.adj[start]:
            self.adj[start].append(end)
        self.weights[(start, end)] = w

    def get_num_of_nodes(self) -> int:
        return len(self.adj)

    def w(self, node1: int, node2: int) -> float:
        connected = False

        for neighbour in self.adj[node1]:
            if neighbour == node2:
                connected = True

        if connected:
            return self.weights[(node1, node2)]

    def get_heuristic(self) -> Dict[int, float]:
        return self.heuristic