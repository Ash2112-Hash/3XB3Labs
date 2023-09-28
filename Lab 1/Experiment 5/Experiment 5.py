from good_sorts import quicksort, heapsort, mergesort
import bad_sorts
import matplotlib.pyplot as plt
import timeit
import math
import numpy as np

length = 200
num_swaps = int(length*math.log(length)/2)
average_runs = 50

def test_allSorts(length, num_swaps, average_runs, sortType):
    times = []
    swaps = []
    time = 0

    for i in range(num_swaps):
        L = bad_sorts.create_near_sorted_list(length, 100, i)
        swaps.append(i)

        for i in range(average_runs):
            start = timeit.default_timer()
            sortType(L.copy())
            end = timeit.default_timer()
            time += (end - start)

        times.append(time / average_runs)
    return swaps, times

swaps1, time1 = test_allSorts(length, num_swaps, average_runs, quicksort)
swaps2, time2 = test_allSorts(length, num_swaps, average_runs, mergesort)
swaps3, time3 = test_allSorts(length, num_swaps, average_runs, heapsort)

swap_quick, time_quick = np.array(swaps1), np.array(time1)
swap_merge, time_merge = np.array(swaps2), np.array(time2)
swap_heap, time_heap = np.array(swaps3), np.array(time3)

plt.title("Number of Swaps vs Runtime")
plt.xlabel("Number of Swaps")
plt.ylabel("Runtime (seconds)")

plt.plot(swap_quick, time_quick)
plt.plot(swap_merge, time_merge)
plt.plot(swap_heap, time_heap)
plt.legend(['Quick Sort', 'Merge Sort', 'Heap Sort'])
plt.show()