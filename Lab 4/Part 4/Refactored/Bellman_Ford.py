
import SPAlgorithm, Graph

#BellmanFord class implementing SPAlgorithm interface/ABC
class Bellman_Ford(SPAlgorithm):

    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        dist = {}  # Distance dictionary
        nodes = list(graph.adj.keys())

        # Initialize distances
        for node in nodes:
            dist[node] = float("inf")
        dist[source] = 0

        # Meat of the algorithm
        for _ in range(graph.number_of_nodes()):
            for node in nodes:
                for neighbour in graph.adj[node]:
                    if dist[neighbour] > dist[node] + graph.w(node, neighbour):
                        dist[neighbour] = dist[node] + graph.w(node, neighbour)

        return dist[dest]


