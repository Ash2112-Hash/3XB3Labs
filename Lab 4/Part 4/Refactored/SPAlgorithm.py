from abc import ABC, abstractmethod

import Graph

#SPAlgorithm interface/ABC
class SPAlgorithm(ABC):

    @abstractmethod
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        pass


