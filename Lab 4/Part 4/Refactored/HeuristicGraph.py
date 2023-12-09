from typing import Dict

import WeightedGraph

#HeursiticGraph class extending from WeightedGraph class
class HeuristicGraph(WeightedGraph):

    def __init__(self):
        self.adj = {}
        self.weights = {}
        self.heuristic: Dict[int, float] = {}

    def get_heuristic(self) -> Dict[int, float]:
        return self.heuristic