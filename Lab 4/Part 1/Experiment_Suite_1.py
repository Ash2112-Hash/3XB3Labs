""" Experiment 1:
Functions and cases to test and compare dijkstra and bellman ford approximation algorithms to their original counterparts
"""
from graph_algs import *
from final_project_part1 import *
import timeit
import matplotlib.pyplot as plot

# Function to display the runtime of dijkstra and its approximations with increasing graph sizes (increasing node count using provided random complete graph function) (Procedure 1)
def plot_DijikstraRuntimeResults(test_runs, average_runs, increase_nodeFactor):
    node_quantities = []
    org_dijkstraTimes = []
    approxk2_dijkstraTimes = []
    approxk3_dijkstraTimes = []
    approxk8_dijkstraTimes = []
    node_count = 1
    # lists to store nodes and algorithm runtimes for plotting

    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        dijkstra_sum = 0
        approxDijkstrak2_sum = 0
        approxDijkstrak3_sum = 0
        approxDijkstrak8_sum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = create_random_complete_graph(node_count, 10)

            start_time = timeit.default_timer()
            dijkstra(G, 0)
            end_time = timeit.default_timer()
            dijkstra_sum += (end_time - start_time)

            #measures the approximation runtimes by setting different values of k
            start_time = timeit.default_timer()
            dijkstra_approx(G, 0, 2)
            end_time = timeit.default_timer()
            approxDijkstrak2_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            dijkstra_approx(G, 0, 3)
            end_time = timeit.default_timer()
            approxDijkstrak3_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            dijkstra_approx(G, 0, 8)
            end_time = timeit.default_timer()
            approxDijkstrak8_sum += (end_time - start_time)


        # appends the results to the corresponding lists
        node_quantities.append(node_count)
        org_dijkstraTimes.append(dijkstra_sum/average_runs)
        approxk2_dijkstraTimes.append(approxDijkstrak2_sum/average_runs)
        approxk3_dijkstraTimes.append(approxDijkstrak3_sum / average_runs)
        approxk8_dijkstraTimes.append(approxDijkstrak8_sum / average_runs)
        node_count += (increase_nodeFactor-1)

    # plots runtime and node quantities of graph
    plot.plot(node_quantities, org_dijkstraTimes, label='Original Dijkstra', marker ='o')
    plot.plot(node_quantities, approxk2_dijkstraTimes, label='Dijkstra Approx (k=2)', marker='o')
    plot.plot(node_quantities, approxk3_dijkstraTimes, label='Dijkstra Approx (k=3)', marker='o')
    plot.plot(node_quantities, approxk8_dijkstraTimes, label='Dijkstra Approx (k=8)', marker='o')
    plot.legend(loc='upper left', title='Pathfinder Algorithms', fontsize=10)
    plot.xlabel('Number of Nodes (N nodes)')
    plot.ylabel('Runtime (s)')
    plot.title("Runtime of Original Dijkstra vs. Approximate Dijkstra algorithms \n with Increasing Graph Size")
    plot.show()


# Function to display the runtime of bellman ford and its approximations with increasing graph sizes (increasing node count using provided random complete graph function) (Procedure 1)
def plot_BellmanRuntimeResults(test_runs, average_runs, increase_nodeFactor):
    node_quantities = []
    org_bellmanTimes = []
    approxk2_bellmanTimes = []
    approxk3_bellmanTimes = []
    approxk8_bellmanTimes = []
    node_count = 1
    # lists to store nodes and algorithm runtimes for plotting

    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        bellman_sum = 0
        approxBellmank2_sum = 0
        approxBellmank3_sum = 0
        approxBellmank8_sum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = create_random_complete_graph(node_count, 10)

            start_time = timeit.default_timer()
            bellman_ford(G, 0)
            end_time = timeit.default_timer()
            bellman_sum += (end_time - start_time)

            # measures the approximation runtimes by setting different values of k
            start_time = timeit.default_timer()
            bellman_ford_approx(G, 0, 2)
            end_time = timeit.default_timer()
            approxBellmank2_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            bellman_ford_approx(G, 0, 3)
            end_time = timeit.default_timer()
            approxBellmank3_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            bellman_ford_approx(G, 0, 6)
            end_time = timeit.default_timer()
            approxBellmank8_sum += (end_time - start_time)


        # appends the results to the corresponding lists
        node_quantities.append(node_count)
        org_bellmanTimes.append(bellman_sum/average_runs)
        approxk2_bellmanTimes.append(approxBellmank2_sum/average_runs)
        approxk3_bellmanTimes.append(approxBellmank3_sum / average_runs)
        approxk8_bellmanTimes.append(approxBellmank8_sum / average_runs)
        node_count += (increase_nodeFactor-1)

    # plots runtime and node quantities of graph
    plot.plot(node_quantities, org_bellmanTimes, label='Original Bellman Ford', marker ='o')
    plot.plot(node_quantities, approxk2_bellmanTimes, label='Bellman Ford Approx (k=2)', marker='o')
    plot.plot(node_quantities, approxk3_bellmanTimes, label='Bellman Ford Approx (k=3)', marker='o')
    plot.plot(node_quantities, approxk8_bellmanTimes, label='Bellman Ford Approx (k=8)', marker='o')
    plot.legend(loc='upper left', title='Pathfinder Algorithms', fontsize=10)
    plot.xlabel('Number of Nodes (N nodes)')
    plot.ylabel('Runtime (s)')
    plot.title("Runtime of Original Bellman Ford vs. Approximate BellmanFord algorithms \n with Increasing Graph Size")
    plot.show()


# Function to display the runtime of dijkstra and its approximations with increasing graph density (increasing edge count using custom random graph function) (Procedure 2)
def plot_DijikstraRuntimeResults2(test_runs, average_runs, increase_edgeFactor):
    edge_quantities = []
    org_dijkstraTimes = []
    approxk2_dijkstraTimes = []
    approxk3_dijkstraTimes = []
    approxk8_dijkstraTimes = []
    node_count = 50
    edge_count = 0
    # lists to store edges and algorithm runtimes for plotting


    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        dijkstra_sum = 0
        approxDijkstrak2_sum = 0
        approxDijkstrak3_sum = 0
        approxDijkstrak8_sum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = generateNonComplete_RandomDirectedGraph(node_count, edge_count, 100)

            start_time = timeit.default_timer()
            dijkstra(G, 0)
            end_time = timeit.default_timer()
            dijkstra_sum += (end_time - start_time)

            # measures the approximation runtimes by setting different values of k
            start_time = timeit.default_timer()
            dijkstra_approx(G, 0, 2)
            end_time = timeit.default_timer()
            approxDijkstrak2_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            dijkstra_approx(G, 0, 3)
            end_time = timeit.default_timer()
            approxDijkstrak3_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            dijkstra_approx(G, 0, 8)
            end_time = timeit.default_timer()
            approxDijkstrak8_sum += (end_time - start_time)


        # appends the results to the corresponding lists
        edge_quantities.append(edge_count)
        org_dijkstraTimes.append(dijkstra_sum/average_runs)
        approxk2_dijkstraTimes.append(approxDijkstrak2_sum / average_runs)
        approxk3_dijkstraTimes.append(approxDijkstrak3_sum / average_runs)
        approxk8_dijkstraTimes.append(approxDijkstrak8_sum / average_runs)
        edge_count += increase_edgeFactor

    # plots probability and edge quantities of graph
    plot.plot(edge_quantities, org_dijkstraTimes, label='Original Dijkstra', marker ='o')
    plot.plot(edge_quantities, approxk2_dijkstraTimes, label='Dijkstra Approx (k=2)', marker='o')
    plot.plot(edge_quantities, approxk3_dijkstraTimes, label='Dijkstra Approx (k=3)', marker='o')
    plot.plot(edge_quantities, approxk8_dijkstraTimes, label='Dijkstra Approx (k=8)', marker='o')
    plot.legend(loc='upper left', title='Pathfinder Algorithms', fontsize=10)
    plot.xlabel('Number of Edges (E edges)')
    plot.ylabel('Runtime (s)')
    plot.title("Runtime of Original Dijkstra vs. Approximate Dijkstra algorithms \n with Increasing Graph Density")
    plot.show()


# Function to display the runtime of bellman ford and its approximations with increasing graph densities (increasing edge count using custom random graph function) (Procedure 2)
def plot_BellmanRuntimeResults2(test_runs, average_runs, increase_edgeFactor):
    edge_quantities = []
    org_bellmanTimes = []
    approxk2_bellmanTimes = []
    approxk3_bellmanTimes = []
    approxk8_bellmanTimes = []
    node_count = 50
    edge_count = 0
    # lists to store edges and algorithm runtimes for plotting


    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        bellman_sum = 0
        approxBellmank2_sum = 0
        approxBellmank3_sum = 0
        approxBellmank8_sum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = generateNonComplete_RandomDirectedGraph(node_count, edge_count, 100)
            # TODO confirm if we need this new random graph function, otherwise replace with given

            start_time = timeit.default_timer()
            bellman_ford(G, 0)
            end_time = timeit.default_timer()
            bellman_sum += (end_time - start_time)

            # measures the approximation runtimes by setting different values of k
            start_time = timeit.default_timer()
            bellman_ford_approx(G, 0, 2)
            end_time = timeit.default_timer()
            approxBellmank2_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            bellman_ford_approx(G, 0, 3)
            end_time = timeit.default_timer()
            approxBellmank3_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            bellman_ford_approx(G, 0, 6)
            end_time = timeit.default_timer()
            approxBellmank8_sum += (end_time - start_time)


        # appends the results to the corresponding lists
        edge_quantities.append(edge_count)
        org_bellmanTimes.append(bellman_sum/average_runs)
        approxk2_bellmanTimes.append(approxBellmank2_sum / average_runs)
        approxk3_bellmanTimes.append(approxBellmank3_sum / average_runs)
        approxk8_bellmanTimes.append(approxBellmank8_sum / average_runs)
        edge_count += increase_edgeFactor

    # plots probability and edge quantities of graph
    plot.plot(edge_quantities, org_bellmanTimes, label='Original Bellman Ford', marker ='o')
    plot.plot(edge_quantities, approxk2_bellmanTimes, label='Bellman Ford Approx (k=2)', marker='o')
    plot.plot(edge_quantities, approxk3_bellmanTimes, label='Bellman Ford Approx (k=3)', marker='o')
    plot.plot(edge_quantities, approxk8_bellmanTimes, label='Bellman Ford Approx (k=8)', marker='o')
    plot.legend(loc='upper left', title='Pathfinder Algorithms', fontsize=10)
    plot.xlabel('Number of Edges (E edges)')
    plot.ylabel('Runtime (s)')
    plot.title("Runtime of Original Bellman Ford vs. Approximate BellmanFord algorithms \n with Increasing Graph Density")
    plot.show()


# Function to indicate the accuracy of the dijkstra/bellman ford algorithms in constrast to their counterpart based on returned graph path
# Quotient: Approximation returned Distance/Original returned Distance will indicate accuracy of algorithm pairs
def plot_AllKResults(test_runs, average_runs):
    k_values = []
    Dijkstradistance_factors = []
    Bellmandistance_factors = []
    node_count = 100
    k = 0
    # lists to store values of k and distance factors

    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        DijkstradistanceFactorSum = 0
        BellmandistanceFactorSum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = create_random_complete_graph(node_count, 100)

            # acquires the distance of the paths and computes corresponding distances
            Dijkorg_Path = dijkstra(G, 0)
            Dijkapprox_Path = dijkstra_approx(G, 0, k)

            Dijkorg_PathDistance = total_dist(Dijkorg_Path)
            Dijkapprox_PathDistance = total_dist(Dijkapprox_Path)
            DijkstradistanceFactorSum += Dijkapprox_PathDistance/Dijkorg_PathDistance

            Bellmanorg_Path = bellman_ford(G, 0)
            Bellmanapprox_Path = bellman_ford_approx(G, 0, k)

            Bellmanorg_PathDistance = total_dist(Bellmanorg_Path)
            Bellmanapprox_PathDistance = total_dist(Bellmanapprox_Path)
            BellmandistanceFactorSum += Bellmanapprox_PathDistance/Bellmanorg_PathDistance


        # appends the results to the corresponding lists
        Dijkstradistance_factors.append(DijkstradistanceFactorSum/average_runs)
        Bellmandistance_factors.append(BellmandistanceFactorSum/average_runs)
        k_values.append(k)
        k += 1

    # plots probability and edge quantities of graph
    plot.plot(k_values, Dijkstradistance_factors, label='Dijkstra Distance Quotient', marker ='o')
    plot.plot(k_values, Bellmandistance_factors, label='Bellman-Ford Distance Quotient', marker='o')
    plot.legend(loc='upper right', title='Algorithm Quotients', fontsize=10)
    plot.xlabel('k')
    plot.ylabel('Quotient (Approximation Distance/Original Distance)')
    plot.title("Accuracy of Original Dijkstra, Bellman Ford vs. Approximate counterpart Algorithms \n with Increasing Node Relaxations")
    plot.show()


# 1.	Increaisng amount of edges increases the amount of possible relaxations:k but we have a better runtime because k is constrained to a limit, otherwise, it would be closer to original
# have sp of spalg interface call original A_star for adapter pattern

def Procedure1():
    plot_DijikstraRuntimeResults(10, 5, 50)
    plot_BellmanRuntimeResults(10, 5, 20)

def Procedure2():
    plot_DijikstraRuntimeResults2(50, 15, 20)
    plot_BellmanRuntimeResults2(50, 15, 20)

def Procedure3():
    plot_AllKResults(15, 5)

Procedure1()
Procedure2()
Procedure3()