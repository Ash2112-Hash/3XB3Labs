""" Experiment 1:
Functions and cases to test and compare brute force and recursive knapsack solutions.
"""

# import libraries needed for experiments
import timeit
from knapsack import *
import matplotlib.pyplot as plot


# function which plots the runtimes results comparing the brute-force and recursive knapsack algorithm
def plotExpResults(test_runs, average_runs, increaseItemFactor, minW, maxW, minVal, maxVal):
    weightMin = minW
    weightMax = maxW
    valueMin = minVal
    valueMax = maxVal
    numItems = 0
    capacity = (maxW + (maxW + 1000))/2
    # parameters for generating the random list

    # lists to store the average runtimes computed for each knapsack alg
    brute_forceTimes = []
    rec_Times = []
    item_lens = []

    # iterates over the specified number of test runs, creates a new random item list and measures the average runtime of each algorithm
    # adds the measured runtime to each corresponding result list
    for num in range(test_runs):
        L_items = createRandomTupleList(numItems, valueMin, valueMax, weightMin, weightMax)
        brute_forceTimeSum = 0
        recTimeSum = 0

        for avg_run in range(average_runs):
            start_time = timeit.default_timer()
            ks_brute_force(L_items, capacity)
            end_time = timeit.default_timer()
            brute_forceTimeSum += (end_time - start_time)

        for avg_run in range(average_runs):
            start_time = timeit.default_timer()
            ks_rec(L_items, capacity)
            end_time = timeit.default_timer()
            recTimeSum += (end_time - start_time)

        item_lens.append(len(L_items))
        brute_forceTimes.append(brute_forceTimeSum / average_runs)
        rec_Times.append(recTimeSum / average_runs)

        # increases the list's item size by a corresponding factor
        numItems += increaseItemFactor

    #finally, plot the resulting runtimes against item sizes
    plot.plot(item_lens, brute_forceTimes, label='Brute Force Algorithm')
    plot.plot(item_lens, rec_Times, label='Recursive Algorithm')
    plot.legend(loc='upper left', title='Knapsack Algorithms', fontsize=10)
    plot.xlabel('Number of Items (n items)')
    plot.ylabel('Runtime (seconds)')
    plot.title("Recursive vs. Brute Force Knapsack Algorithm")
    plot.show()

# Conduct the two test cases
plotExpResults(5, 5, 1, 20, 75, 1000, 2000)
plotExpResults(20, 5, 1, 20, 75, 1000, 2000)
