import timeit
import matplotlib.pyplot as plot
from knapsack import *

def TDvsBU(average_runs):
    capacity = 50
    valMin, weightMin = 0, 0
    valMax, weightMax = 100, 100

    list_lens = [n for n in range(1, 700)]
    BU_times = []
    TD_times = []

    for n in list_lens:
        BU_sum, TD_sum = 0, 0

        for _ in range(average_runs):
            items = createRandomTupleList(n, valMin, valMax, weightMin, weightMax)
            
            start_time = timeit.default_timer()
            BU = ks_bottom_up(items, capacity)
            end_time = timeit.default_timer()
            BU_sum += (end_time - start_time)  

            start_time = timeit.default_timer()
            TD = ks_top_down(items, capacity)
            end_time = timeit.default_timer()
            TD_sum += (end_time - start_time)

        BU_times.append(BU_sum/average_runs)
        TD_times.append(TD_sum/average_runs)  

    plot.plot(list_lens, BU_times, label = 'Bottom Up Approach')
    plot.plot(list_lens, TD_times, label = 'Top Down Approach')
    plot.legend(loc = 'upper left', title = 'Dynamic Programming Approach', fontsize = 10)
    plot.xlabel('Number of Items (n elements)')
    plot.ylabel('Runtime (seconds)')
    plot.title("Runtime vs Number of Items")
    plot.show()

def BUvsTD(average_runs):
    capacity = 50
    valMin, weightMin = 0, 0
    valMax, weightMax = 2000, 2000

    list_lens = [n for n in range(1, 500)]
    BU_times = []
    TD_times = []

    for n in list_lens:
        BU_sum, TD_sum = 0, 0

        for _ in range(average_runs):
            items = createRandomTupleList(n, valMin, valMax, weightMin, weightMax)
            
            start_time = timeit.default_timer()
            BU = ks_bottom_up(items, capacity)
            end_time = timeit.default_timer()
            BU_sum += (end_time - start_time)  

            start_time = timeit.default_timer()
            TD = ks_top_down(items, capacity)
            end_time = timeit.default_timer()
            TD_sum += (end_time - start_time)
            assert BU == TD

        BU_times.append(BU_sum/average_runs)
        TD_times.append(TD_sum/average_runs)  

    plot.plot(list_lens, BU_times, label = 'Bottom Up Approach')
    plot.plot(list_lens, TD_times, label = 'Top Down Approach')
    plot.legend(loc = 'upper left', title = 'Dynamic Programming Approach', fontsize=10)
    plot.xlabel('Number of Items (n elements)')
    plot.ylabel('Runtime (seconds)')
    plot.title("Runtime vs Number of Items")
    plot.show()