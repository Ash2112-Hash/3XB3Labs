""" Experiment 1:
Functions and cases to test and compare dijkstra and bellman ford approximation algorithms to their original counterparts
"""
from graph_algs import *
from final_project_part1 import *
import timeit
import matplotlib.pyplot as plot


def plot_DijikstraRuntimeResults(test_runs, average_runs, increase_nodeFactor):
    node_quantities = []
    org_dijkstraTimes = []
    approx_dijkstraTimes = []
    node_count = 1
    # lists to store nodes and algorithm runtimes for plotting


    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        dijkstra_sum = 0
        approxDijkstra_sum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = create_random_complete_graph(node_count, 10)

            start_time = timeit.default_timer()
            dijkstra(G, 0)
            end_time = timeit.default_timer()
            dijkstra_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            dijkstra_approx(G, 0, 3)
            end_time = timeit.default_timer()
            approxDijkstra_sum += (end_time - start_time)


        # appends the results to the corresponding lists
        node_quantities.append(node_count)
        org_dijkstraTimes.append(dijkstra_sum/average_runs)
        approx_dijkstraTimes.append(approxDijkstra_sum/average_runs)
        node_count += (increase_nodeFactor-1)

    # plots probability and edge quantities of graph
    plot.plot(node_quantities, org_dijkstraTimes, label='Original Dijkstra', marker ='o')
    plot.plot(node_quantities, approx_dijkstraTimes, label='Dijkstra Approx', marker='o')
    plot.legend(loc='upper left', title='Pathfinder Algorithms', fontsize=10)
    plot.xlabel('Number of Nodes (N nodes)')
    plot.ylabel('Runtime (s)')
    plot.title("Runtime of Original Dijkstra vs. Approximate Dijkstra algorithms \n with Increasing Graph Size")
    plot.show()



def plot_BellmanRuntimeResults(test_runs, average_runs, increase_nodeFactor):
    node_quantities = []
    org_bellmanTimes = []
    approx_bellmanTimes = []
    node_count = 1
    # lists to store nodes and algorithm runtimes for plotting


    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        bellman_sum = 0
        approxBellman_sum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = create_random_complete_graph(node_count, 10)

            start_time = timeit.default_timer()
            bellman_ford(G, 0)
            end_time = timeit.default_timer()
            bellman_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            bellman_ford_approx(G, 0, 3)
            end_time = timeit.default_timer()
            approxBellman_sum += (end_time - start_time)


        # appends the results to the corresponding lists
        node_quantities.append(node_count)
        org_bellmanTimes.append(bellman_sum/average_runs)
        approx_bellmanTimes.append(approxBellman_sum/average_runs)
        node_count += (increase_nodeFactor-1)

    # plots probability and edge quantities of graph
    plot.plot(node_quantities, org_bellmanTimes, label='Original Bellman Ford', marker ='o')
    plot.plot(node_quantities, approx_bellmanTimes, label='Bellman Ford Approx', marker='o')
    plot.legend(loc='upper left', title='Pathfinder Algorithms', fontsize=10)
    plot.xlabel('Number of Nodes (N nodes)')
    plot.ylabel('Runtime (s)')
    plot.title("Runtime of Original Bellman Ford vs. Approximate BellmanFord algorithms \n with Increasing Graph Size")
    plot.show()



def plot_DijikstraRuntimeResults2(test_runs, average_runs, increase_edgeFactor):
    edge_quantities = []
    org_dijkstraTimes = []
    approx_dijkstraTimes = []
    node_count = 50
    edge_count = 0
    # lists to store edges and algorithm runtimes for plotting


    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        dijkstra_sum = 0
        approxDijkstra_sum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = generateNonComplete_RandomDirectedGraph(node_count, edge_count, 100)
            #TODO confirm if we need this new random graph function, otherwise replace with given

            start_time = timeit.default_timer()
            dijkstra(G, 0)
            end_time = timeit.default_timer()
            dijkstra_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            dijkstra_approx(G, 0, 3)
            end_time = timeit.default_timer()
            approxDijkstra_sum += (end_time - start_time)


        # appends the results to the corresponding lists
        edge_quantities.append(edge_count)
        org_dijkstraTimes.append(dijkstra_sum/average_runs)
        approx_dijkstraTimes.append(approxDijkstra_sum/average_runs)
        edge_count += increase_edgeFactor

    # plots probability and edge quantities of graph
    plot.plot(edge_quantities, org_dijkstraTimes, label='Original Dijkstra', marker ='o')
    plot.plot(edge_quantities, approx_dijkstraTimes, label='Dijkstra Approx', marker='o')
    plot.legend(loc='upper left', title='Pathfinder Algorithms', fontsize=10)
    plot.xlabel('Number of Edges (E edges)')
    plot.ylabel('Runtime (s)')
    plot.title("Runtime of Original Dijkstra vs. Approximate Dijkstra algorithms \n with Increasing Graph Density")
    plot.show()


def plot_BellmanRuntimeResults2(test_runs, average_runs, increase_edgeFactor):
    edge_quantities = []
    org_bellmanTimes = []
    approx_bellmanTimes = []
    node_count = 50
    edge_count = 0
    # lists to store edges and algorithm runtimes for plotting


    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        bellman_sum = 0
        approxBellman_sum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = generateNonComplete_RandomDirectedGraph(node_count, edge_count, 100)
            # TODO confirm if we need this new random graph function, otherwise replace with given

            start_time = timeit.default_timer()
            bellman_ford(G, 0)
            end_time = timeit.default_timer()
            bellman_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            bellman_ford_approx(G, 0, 3)
            end_time = timeit.default_timer()
            approxBellman_sum += (end_time - start_time)


        # appends the results to the corresponding lists
        edge_quantities.append(edge_count)
        org_bellmanTimes.append(bellman_sum/average_runs)
        approx_bellmanTimes.append(approxBellman_sum/average_runs)
        edge_count += increase_edgeFactor

    # plots probability and edge quantities of graph
    plot.plot(edge_quantities, org_bellmanTimes, label='Original Bellman Ford', marker ='o')
    plot.plot(edge_quantities, approx_bellmanTimes, label='Bellman Ford Approx', marker='o')
    plot.legend(loc='upper left', title='Pathfinder Algorithms', fontsize=10)
    plot.xlabel('Number of Edges (E edges)')
    plot.ylabel('Runtime (s)')
    plot.title("Runtime of Original Bellman Ford vs. Approximate BellmanFord algorithms \n with Increasing Graph Density")
    plot.show()


def plot_DijikstraKResults(test_runs, average_runs):
    k_values = []
    Dijkstradistance_factors = []
    Bellmandistance_factors = []
    node_count = 50
    k = 0
    # lists to store values of k and distance factors

    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        DijkstradistanceFactorSum = 0
        BellmandistanceFactorSum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = create_random_complete_graph(node_count, 100)

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
    plot.ylabel('Quotient (Original path/Approx path)')
    plot.title("Accuracy of Original Dijkstra, Bellman Ford vs. Approximate counterpart Algorithms \n with Increasing Node Relaxations")
    plot.show()




def plot_AllKResults(test_runs, average_runs):
    k_values = []
    Dijkstradistance_factors = []
    Bellmandistance_factors = []
    node_count = 50
    k = 0
    # lists to store values of k and distance factors

    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        DijkstradistanceFactorSum = 0
        BellmandistanceFactorSum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = create_random_complete_graph(node_count, 100)

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
    plot.ylabel('Quotient (Original path/Approx path)')
    plot.title("Accuracy of Original Dijkstra, Bellman Ford vs. Approximate counterpart Algorithms \n with Increasing Node Relaxations")
    plot.show()




def plot_AllKRuntimeResults(test_runs, average_runs):
    k_values = []
    Dijkstradistance_factors = []
    Bellmandistance_factors = []
    node_count = 50
    k = 0
    # lists to store values of k and distance factors

    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        DijkstradistanceFactorSum = 0
        BellmandistanceFactorSum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = create_random_complete_graph(node_count, 100)

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
    plot.ylabel('Quotient (Original path/Approx path)')
    plot.title("Accuracy of Original Dijkstra, Bellman Ford vs. Approximate counterpart Algorithms \n with Increasing Node Relaxations")
    plot.show()



def Procedure1():
    plot_DijikstraRuntimeResults(10, 3, 50)
    plot_BellmanRuntimeResults(10, 3, 20)   #TODO confirm the alg for bellman approx

def Procedure2():
    plot_DijikstraRuntimeResults2(50, 10, 20)  #TODO confirm if same nature is seen in the runtime
    plot_DijikstraRuntimeResults2(80, 10, 20)  # TODO confirm if same nature is seen in the runtime

    plot_BellmanRuntimeResults2(20, 10, 20)   #TODO confirm if same nature is seen in the runtime
    plot_BellmanRuntimeResults2(40, 10, 20)

def Procedure3():
    plot_AllKResults(15, 5)

def Procedure4():
    pass

#Procedure1()
#Procedure2()
#Procedure3()