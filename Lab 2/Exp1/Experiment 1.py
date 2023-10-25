# ******************* Experiment 1 *******************
# Functions and methodology designated to running experiment 1 involving cycles in random graphs

# Imports the following libraries required for the experiment functions
import matplotlib.pyplot as plot
from graph import *

def plot_RandomGCycleProb(average_runs, node_count, edge_count):
    edge_quantities = []
    cycle_probs = []
    maxEdges = int(node_count * ((node_count-1)/2))
    num_edges = maxEdges if edge_count > maxEdges else edge_count

    for edge_num in range(0, num_edges + 1, 2):
        cycleProbCounter = 0

        for _ in range(average_runs):
            G = create_random_graph(node_count, edge_num)
            #print(G.adj)
            #print(G.number_of_nodes())

            if(has_cycle(G)):
                cycleProbCounter += 1

        cycle_probs.append(cycleProbCounter/average_runs)
        edge_quantities.append(edge_num)
        #print(cycle_probs)

    plot.plot(edge_quantities, cycle_probs, label='Cycle Probability')
    plot.xlabel('Number of Edges (n edges)')
    plot.ylabel('Cycle Probability')
    plot.title("Probability of Cycle within Random Graph based on Edge Quantity")
    plot.show()


def main():
    plot_RandomGCycleProb(10, 10, 10)
    plot_RandomGCycleProb(20, 50, 30)
    plot_RandomGCycleProb(20, 60, 100)


main()

