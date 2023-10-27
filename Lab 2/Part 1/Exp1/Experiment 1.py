# ******************* Experiment 1 *******************
# Functions and methodology designated to running experiment 1 involving cycles in random graphs

# Imports the following libraries required for the experiment functions
import matplotlib.pyplot as plot
from graph import *


# plot_RandomGCycleProb plots the probability of a cycle being detected within a randomly generated graph over a specified number of average runs, nodes, edges and a increasing edge factor
def plot_RandomGCycleProb(average_runs, node_count, edge_count, increase_edgeFactor):
    edge_quantities = []
    cycle_probs = []
    # lists to store edges and cycle probabilities for plotting

    maxEdges = int(node_count * ((node_count-1)/2))
    # max amount of edges based on node count

    num_edges = maxEdges if edge_count > maxEdges else edge_count
    # if provided edges cross maxEdges threshold, set number of edges to maxedges

    # loops through the range of edges and increases them by the specified factor
    for edge_num in range(0, num_edges, increase_edgeFactor):
        cycleProbCounter = 0

        # generates a random graph in each average run and increments the cycle counter if a cycle is detected
        for _ in range(average_runs):
            G = create_random_graph(node_count, edge_num)
            #print(G.adj)
            #print(G.number_of_nodes())

            if has_cycle(G):
                cycleProbCounter += 1

        # appends the cycle probability (average based on average runs) and edges to corresponding lists
        cycle_probs.append(cycleProbCounter/average_runs)
        edge_quantities.append(edge_num)
        #print(cycle_probs)

    # plots probability and edge quantities of graph
    plot.plot(edge_quantities, cycle_probs, label='Cycle Probability', marker = 'o')
    plot.xlabel('Number of Edges (E edges)')
    plot.ylabel('Cycle Probability')
    plot.title("Probability of Cycle within Random Graph(" + str(node_count) + " nodes) based on Edge Quantity")
    plot.show()


# main function to execute all the test cases
def main():
    plot_RandomGCycleProb(30, 10, 10, 2)    # figure 1
    plot_RandomGCycleProb(200, 50, 30, 5)   # figure 2
    plot_RandomGCycleProb(500, 100, 300, 10)  # figure 3
    plot_RandomGCycleProb(30, 10, 45, 2)    # figure 4


main()
# call main

