
from abc import ABC, abstractmethod

# Graph interface/ABC
class Graph(ABC):

    @abstractmethod
    def get_adj_nodes(self, node: int) -> [int]:
        pass

    @abstractmethod
    def add_node(self, node: int):
        pass

    @abstractmethod
    def add_edge(self, start: int, end: int):
        pass

    @abstractmethod
    def get_num_of_nodes(self) -> int:
        pass



