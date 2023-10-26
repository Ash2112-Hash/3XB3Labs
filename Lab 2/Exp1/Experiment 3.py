#graphing MVC vs the other approximations

import graph
import vertexcover
import matplotlib.pyplot as plt

# ******Graphing*******

def vc_test(num_nodes, test_runs):
    # This runs the test that was described in the lab manual under the "approximation experiments" section
    track_edges = []
    mvc_sums = []
    approx1_sums = []
    approx2_sums = []
    approx3_sums = []

    for i in range(31):
        mvc_sum = 0
        approx1_sum = 0
        approx2_sum = 0
        approx3_sum = 0

        for j in range(test_runs):
            G = graph.create_random_graph(num_nodes, i)

            mvc_sum += len(graph.MVC(G))
            approx1_sum += len(vertexcover.approx1(G))
            approx2_sum += len(vertexcover.approx2(G))
            approx3_sum += len(vertexcover.approx3(G))

        mvc_sums.append(mvc_sum)
        approx1_sums.append(approx1_sum)
        approx2_sums.append(approx2_sum)
        approx3_sums.append(approx3_sum)
        track_edges.append(i)


    # plotting the graph
    plt.plot(track_edges, mvc_sums)
    plt.plot(track_edges, approx1_sums)
    plt.plot(track_edges, approx2_sums)
    plt.plot(track_edges, approx3_sums)
    plt.xlabel('Number of Edges')
    plt.ylabel('Sum of Vertex Cover Lengths')
    plt.title('Vertex Cover Lengths Using Different Approximation Methods')
    plt.legend(['Minimum Vertex Cover', 'Approximation 1', 'Approximation 2', 'Approximation 3'])
    plt.show()


def main():
    vc_test(8, 1000)


main()
