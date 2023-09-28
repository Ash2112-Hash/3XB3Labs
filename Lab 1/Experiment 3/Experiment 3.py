import timeit
import matplotlib.pyplot as plt 
import numpy as np
import math
from bad_sorts import *

num_swaps = int(1000*math.log(1000,10)/2)
average_runs = 25

def test_allSorts(num_swaps, average_runs, sortType):
    times = []
    swaps = []

    for i in range(0, num_swaps, 100):
        time = 0

        for _ in range(average_runs):
            L = create_near_sorted_list(1000, 100, i)
            start = timeit.default_timer()
            sortType(L)
            end = timeit.default_timer()
            time += (end - start)
        swaps.append(i)
        times.append(time / average_runs)

    return swaps, times

swaps1, time1 = test_allSorts(num_swaps, average_runs, insertion_sort)
swaps2, time2 = test_allSorts(num_swaps, average_runs, bubble_sort)
swaps3, time3 = test_allSorts(num_swaps, average_runs, selection_sort)

swap_insertion, time_insertion = np.array(swaps1), np.array(time1)
swap_bubble, time_bubble = np.array(swaps2), np.array(time2)
swap_selection, time_selection = np.array(swaps3), np.array(time3)

plt.title("Number of Swaps vs Runtime")
plt.xlabel("Number of Swaps")
plt.ylabel("Runtime (seconds)")

plt.plot(swap_insertion, time_insertion, color = 'r', label = 'Insertion Sort')
plt.plot(swap_bubble, time_bubble, color = 'b', label = 'Bubble Sort')
plt.plot(swap_selection, time_selection, color = 'g', label = 'Selection Sort')
plt.legend()
plt.show()