from good_sorts import quicksort, heapsort, mergesort
import bad_sorts
import matplotlib.pyplot as plt
import timeit
import math
import numpy as np

def test_allSorts(sortType):
    length = 500
    num_swaps = int(length*math.log(length, 10)/2)
    max_value = 100
    average_runs = 25
    
    times = []
    swaps = []

    for i in range(0, num_swaps, 100): #resets timer for each algorithm
        time = 0

        for j in range(average_runs): #running multiple tests for accuracy
            L = bad_sorts.create_near_sorted_list(length, max_value, i)
            start = timeit.default_timer()
            sortType(L)
            end = timeit.default_timer()
            time += (end - start)

        swaps.append(i)
        times.append(time / average_runs)

    return swaps, times

#swaps = x-axis, time = y-axis
swaps1, time1 = test_allSorts(quicksort)
swaps2, time2 = test_allSorts(mergesort)
swaps3, time3 = test_allSorts(heapsort)

swap_quick, time_quick = np.array(swaps1), np.array(time1)
swap_merge, time_merge = np.array(swaps2), np.array(time2)
swap_heap, time_heap = np.array(swaps3), np.array(time3)

#plotting the graph
plt.title("Number of Swaps vs Runtime of Good Sorting Algorithms")
plt.xlabel("Number of Swaps")
plt.ylabel("Runtime (seconds)")

plt.plot(swap_quick, time_quick)
plt.plot(swap_merge, time_merge)
plt.plot(swap_heap, time_heap)
plt.legend(['Quick Sort', 'Merge Sort', 'Heap Sort'])
plt.show()