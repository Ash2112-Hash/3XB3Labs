#graphing MVC vs the other approximations

import graph
import vertexcover
import matplotlib.pyplot as plt


'''
# ******Graphing*******

def test_connected(num_nodes, num_edges, test_runs):
    probabilities = []
    connected_or_not = []
    track_edges = []

    for i in range(0, num_edges + 1, 2):

        for j in range(test_runs):
            G = graph.create_random_graph(num_nodes, i)
            connected = graph.Is_connected(G)
            connected_or_not.append(connected)

        counter = 0
        for element in connected_or_not:
            if element == True:
                counter += 1
        
        probability = counter / len(connected_or_not)
        probabilities.append(probability)

        track_edges.append(i)


    #plotting the graph
    plt.plot(track_edges, probabilities)
    plt.xlabel('Number of Edges')
    plt.ylabel('Likelihood')
    plt.title('Likelihood of Graph Being Connected With ' + str(num_nodes) + ' Nodes')
    plt.show()
    return None
'''
def main():
    G = graph.create_random_graph(7, 9)
    H = graph.create_random_graph(10, 23)
    I = graph.create_random_graph(20, 20)

    C = vertexcover.approx2(G)
    D = vertexcover.approx2(H)
    E = vertexcover.approx2(I)

    for item in C:
        print(item)

    for item in D:
        print(item)

    for item in E:
        print(item)
        
main()