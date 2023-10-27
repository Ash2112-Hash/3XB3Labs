#graphing MVC vs the other approximations

from graph import *
from vertexcover import *
import matplotlib.pyplot as plt


# ******Graphing*******
def vce_test(num_nodes, test_runs, num_edges, edgeIncrease_factor):
    # This finds the average VC length for graphs with a constant number of nodes, but increasing edges
    track_edges = []
    approx1_sums = []
    approx2_sums = []
    approx3_sums = []
    MVC_sums = []

    for i in range(0, num_edges + 1, edgeIncrease_factor):
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

        if MVC_sum == 0:
            MVC_sums.append(0)
            approx1_sums.append(approx1_sum)
            approx2_sums.append(approx2_sum)
            approx3_sums.append(approx3_sum)
        else:
            MVC_sums.append(MVC_sum / MVC_sum)
            approx1_sums.append(approx1_sum / MVC_sum)
            approx2_sums.append(approx2_sum / MVC_sum)
            approx3_sums.append(approx3_sum / MVC_sum)

        track_edges.append(i)


    # plotting the graph
    plt.plot(track_edges, MVC_sums)
    plt.plot(track_edges, approx1_sums)
    plt.plot(track_edges, approx2_sums)
    plt.plot(track_edges, approx3_sums)
    plt.xlabel('Number of Edges')
    plt.ylabel('Expected Performance')
    plt.title('Expected VC Approximation Performance for Graphs with ' + str(num_nodes) + ' Nodes')
    plt.legend(['Minimum Vertex Cover', 'Approximation 1', 'Approximation 2', 'Approximation 3'])
    plt.show()

def vcn_test(num_nodes, test_runs, num_edges, nodeIncrease_factor):
    # This finds the average VC length for graphs with a constant number of edges, but increasing nodes
    track_nodes = []
    approx1_sums = []
    approx2_sums = []
    approx3_sums = []
    MVC_sums = []

    for i in range(0, num_nodes + 1, nodeIncrease_factor):
        MVC_sum = 0
        approx1_sum = 0
        approx2_sum = 0
        approx3_sum = 0

        for j in range(test_runs):
            G = create_random_graph(i, num_edges)

            MVC_sum += len(MVC(G))
            approx1_sum += len(approx1(G))
            approx2_sum += len(approx2(G))
            approx3_sum += len(approx3(G))

        if MVC_sum == 0:
            MVC_sums.append(0)
            approx1_sums.append(approx1_sum)
            approx2_sums.append(approx2_sum)
            approx3_sums.append(approx3_sum)
        else:
            MVC_sums.append(MVC_sum / MVC_sum)
            approx1_sums.append(approx1_sum / MVC_sum)
            approx2_sums.append(approx2_sum / MVC_sum)
            approx3_sums.append(approx3_sum / MVC_sum)
        
        track_nodes.append(i)


    # plotting the graph
    plt.plot(track_nodes, MVC_sums)
    plt.plot(track_nodes, approx1_sums)
    plt.plot(track_nodes, approx2_sums)
    plt.plot(track_nodes, approx3_sums)
    plt.xlabel('Number of Nodes')
    plt.ylabel('Expected Performance')
    plt.title('Expected VC Approximation Performance for Graphs with ' + str(num_edges) + ' Edges')
    plt.legend(['Minimum Vertex Cover', 'Approximation 1', 'Approximation 2', 'Approximation 3'])
    plt.show()


def main():
    vce_test(4, 1000, 30, 5)
    vce_test(10, 1000, 30, 5)

    vcn_test(10, 1000, 15, 2)
    vcn_test(10, 1000, 30, 2)

main()
