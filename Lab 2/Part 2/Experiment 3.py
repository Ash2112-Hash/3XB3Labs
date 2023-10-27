#graphing MVC vs the other approximations

from graph import *
from vertexcover import *
import matplotlib.pyplot as plt


# ******Graphing*******
def vc_test(num_nodes, test_runs, num_edges, edgeIncrease_factor):
    # This runs the test that was described in the lab manual under the "approximation experiments" section
    track_edges = []
    approx1_sums = []
    approx2_sums = []
    approx3_sums = []
    MVC_sums = []

    for i in range(0, num_edges, edgeIncrease_factor):
        MVC_sum = 0
        approx1_sum = 0
        approx2_sum = 0
        approx3_sum = 0

        for j in range(test_runs):
            G = create_random_graph(num_nodes, i)

            MVC_sum += len(MVC(G))
            approx1_sum += len(approx1(G))
            approx2_sum += len(approx2(G))
            approx3_sum += len(approx3(G))

        MVC_sums.append(MVC_sum / test_runs)
        approx1_sums.append(approx1_sum / test_runs)
        approx2_sums.append(approx2_sum / test_runs)
        approx3_sums.append(approx3_sum / test_runs)
        track_edges.append(i)


    # plotting the graph
    plt.plot(track_edges, MVC_sums)
    plt.plot(track_edges, approx1_sums)
    plt.plot(track_edges, approx2_sums)
    plt.plot(track_edges, approx3_sums)
    plt.xlabel('Number of Edges')
    plt.ylabel('Sum of Vertex Cover Lengths')
    plt.title('Vertex Cover Lengths Using Different Approximation Methods')
    plt.legend(['Minimum Vertex Cover', 'Approximation 1', 'Approximation 2', 'Approximation 3'])
    plt.show()


def main():
    vc_test(8, 1000, 30, 5)
    vc_test(5, 1000, 30, 5)
    vc_test(20, 1000, 30, 5)

main()
