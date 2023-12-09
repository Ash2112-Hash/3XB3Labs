
import SPAlgorithm, Graph, a_star_alg


class A_Star(SPAlgorithm):

    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        G_heuristic = graph.get_heuristic()
        result = a_star_alg.a_star(graph, source, dest, G_heuristic)

        path_dist = 0
        for key in result[1].keys():
            path_dist += result[1][key]

        return path_dist
