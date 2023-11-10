""" Experiment 1:
Functions and cases to test and compare brute force and recursive knapsack solutions.
"""

import timeit
from knapsack import *
import matplotlib.pyplot as plot


def plotExp1Results(test_runs, average_runs, increaseItemFactor):
    weightMin = 20
    weightMax = 75
    valueMin = 1000
    valueMax = 2000
    numItems = 0
    capacity = 0

    # lists to store the average runtimes computed for each knapsack alg
    brute_forceTimes = []
    rec_Times = []
    item_lens = []

    # iterates over the specified number of test runs, creates a new list in each run and conducts average runs for each of the 3 sorting algorithms against the list (in each iteration)
    for num in range(test_runs):
        L_items = createRandomTupleSet(numItems, valueMin, valueMax, weightMin, weightMax)
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

        print(item_lens)
        print(rec_Times)
        print(brute_forceTimes)

        # increases the list's capacity by a corresponding factor
        numItems += increaseItemFactor

    plot.plot(item_lens, brute_forceTimes, label='Brute Force Algorithm')
    plot.plot(item_lens, rec_Times, label='Recursive Algorithm')
    plot.legend(loc='upper left', title='Knapsack Algorithms', fontsize=10)
    plot.xlabel('Number of Items (n items)')
    plot.ylabel('Runtime (seconds)')
    plot.title("Recursive vs. Brute Force Knapsack Algorithm")
    plot.show()


plotExp1Results(5, 5, 1)
plotExp1Results(15, 5, 1)