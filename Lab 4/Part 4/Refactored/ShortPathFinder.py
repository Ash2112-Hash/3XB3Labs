import SPAlgorithm, Graph

# pathfinder class which uses composition pattenr with graph and SPAlgorithm interfaces
class ShortPathFinder:

    def calc_short_path(self, source: int, dest: int) -> float:
        short_pathDist = self.algorithm(self.G, source, dest)
        return short_pathDist

    def set_graph(self, graph: Graph):
        self.G = graph

    def algorithm(self, algorithm: SPAlgorithm):
        self.algorithm = algorithm
