""" Experiment 1:
Functions and cases to test and compare dijkstra and bellman ford approximation algorithms to their original counterparts
"""
from graph_algs import *
from final_project_part1 import *
import timeit
import matplotlib.pyplot as plot


def plot_RuntimeResults(test_runs, average_runs, node_count, increase_nodeFactor):
    node_quantities = []
    org_dijkstraTimes = []
    org_bellmanTimes = []
    approx_dijkstraTimes = []
    approx_bellmanTimes = []
    # lists to store edges and algorithm runtimes for plotting


    # loops through the range of edges and increases them by the specified factor
    for _ in range(test_runs):
        dijkstra_sum = 0
        bellmanford_sum = 0
        approxDijkstra_sum = 0
        approxBellmanford_sum = 0

        # generates a random graph in each average run and acquires the average runtimes
        for _ in range(average_runs):
            G = create_random_complete_graph(node_count, 100)

            start_time = timeit.default_timer()
            dijkstra(G, 0)
            end_time = timeit.default_timer()
            dijkstra_sum += (end_time - start_time)


            start_time = timeit.default_timer()
            bellman_ford(G, 0)
            end_time = timeit.default_timer()
            bellmanford_sum += (end_time - start_time)


            start_time = timeit.default_timer()
            dijkstra_approx(G, 0, 3)
            end_time = timeit.default_timer()
            approxDijkstra_sum += (end_time - start_time)

            start_time = timeit.default_timer()
            bellman_ford_approx(G, 0, 3)
            end_time = timeit.default_timer()
            approxBellmanford_sum += (end_time - start_time)



        # appends the results to the corresponding lists
        node_quantities.append(node_count)
        org_dijkstraTimes.append(dijkstra_sum/average_runs)
        org_bellmanTimes.append(bellmanford_sum/average_runs)
        approx_dijkstraTimes.append(approxDijkstra_sum/average_runs)
        approx_bellmanTimes.append(approxBellmanford_sum/average_runs)
        node_count += increase_nodeFactor

    # plots probability and edge quantities of graph
    plot.plot(node_quantities, org_dijkstraTimes, label='Org Dijkstra', marker = 'o')
    plot.plot(node_quantities, org_bellmanTimes, label='Org Bellman-Ford', marker='o')
    plot.plot(node_quantities, approx_dijkstraTimes, label='Approx Dijkstra', marker='o')
    plot.plot(node_quantities, approx_bellmanTimes, label='Approx Bellman-Ford', marker='o')
    plot.legend(loc='upper left', title='Pathfinder Algorithms', fontsize=10)
    plot.xlabel('Number of Nodes (N nodes)')
    plot.ylabel('Runtime (s)')
    plot.title("Comparing Runtime of Original vs. Approximate pathfinder algorithms with increasing Nodes (k=3)")
    plot.show()


# main function to execute all the test cases
def main():
    plot_RuntimeResults(10, 5, 20, 10)

main()
# call main
