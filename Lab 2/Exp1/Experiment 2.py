import graph
import matplotlib.pyplot as plt


# ******Graphing*******

def test_connected(num_nodes, num_edges, test_runs):
    probabilities = []
    track_edges = []
    maxEdges = int(num_nodes * ((num_nodes - 1) / 2))
    edge_count = maxEdges if num_edges > maxEdges else num_edges

    for i in range(0, edge_count + 1, 2):
        connected_ProbCounter = 0

        for j in range(test_runs):
            G = graph.create_random_graph(num_nodes, i)

            if graph.Is_connected(G):
                connected_ProbCounter += 1

        probabilities.append(connected_ProbCounter / test_runs)
        track_edges.append(i)

    # TODO may need to confirm if method is correct

    # plotting the graph
    plt.plot(track_edges, probabilities)
    plt.xlabel('Number of Edges')
    plt.ylabel('Likelihood')
    plt.title('Likelihood of Graph Being Connected With ' + str(num_nodes) + ' Nodes')
    plt.show()


def main():
    test_connected(20, 60, 100)
    test_connected(40, 80, 100)
    test_connected(100, 200, 100)


main()
