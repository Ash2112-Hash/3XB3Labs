# ******************* Experiment 1 *******************
# Functions and methodology designated to running experiment 1 involving cycles in random graphs

# Imports the following libraries required for the experiment functions
import timeit
import matplotlib.pyplot as plot
from graph import *



def conduct_AverageRuns(averageRunCount):
    prob_sum = 0

    for num in range(averageRunCount):
        #TODO CREATE RANDOM GRAPH
        G = Graph(0)

        if(has_cycle(G)):
            prob_sum+=1



    return prob_sum/averageRunCount




def plot_RandomGCycleProb(test_runs, average_runs):
    edge_quantity = []
    cycle_probs = []
    edge_count = 0


    for each_run in range(test_runs):

        """create random graph
            fix node count to 100
            increase edge count each time - 10
            
        
        """

        Avgcycle_prob = conduct_AverageRuns(average_runs)
        cycle_probs.append(Avgcycle_prob)
        edge_quantity.append(edge_count)
        edge_count += 10



    # plots the runtimes of the 3 sorting algorithms with the following legends and axis titles
    plot.plot(edge_quantity, cycle_probs, label='Cycle Probability')
    plot.xlabel('Number of Edges (n edges)')
    plot.ylabel('Cycle Probability')
    plot.title("Probability of Cycle within Random Graph based on Edge Quantity")
    plot.show()


plot_RandomGCycleProb(10, 10)



