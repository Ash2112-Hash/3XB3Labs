import timeit
import matplotlib.pyplot as plt 
import numpy as np
import math
from bad_sorts import *
from good_sorts import *

def bottom_up_mergesort(L):
    n = len(L)
    size = 1

    if n <= 1:
        return
    
    while size < n:
        # try n - size
        for i in range(0, n, 2 * size):
            left = L[i:i + size]
            right = L[i + size:i + 2 * size]
            merged = merge(left, right)
            L[i:i + 2 * size] = merged
        size *= 2

def test_allSorts(sortMethod, test_runs, increase_list):
    list_len = 0 
    max_value = 100
    average_runs = 100

    times = []
    list_lengths = []

    for i in range(test_runs):
        L = create_random_list(list_len, max_value)
        time = 0

        for _ in range(average_runs):
            start = timeit.default_timer()
            sortMethod(L)
            end = timeit.default_timer()
            time += (end - start)

        list_lengths.append(list_len)
        times.append(time / average_runs)
        list_len += increase_list

    return list_lengths, times

listlen1, time1 = test_allSorts(mergesort, 15, 100)
listlen2, time2 = test_allSorts(bottom_up_mergesort, 15, 100)

listlen_merge, time_merge = np.array(listlen1), np.array(time1)
listlen_bottom_up, time_bottom_up = np.array(listlen2), np.array(time2)

# plotting the data and establishing the graph labels
plt.title("List Length vs Runtime")
plt.xlabel("List Length (n)")
plt.ylabel("Runtime (seconds)")
plt.plot(listlen_merge, time_merge, color = 'r', label = 'Merge Sort')
plt.plot(listlen_bottom_up, time_bottom_up, color = 'b', label = 'Bottom-up Merge Sort')
plt.legend()
plt.show()