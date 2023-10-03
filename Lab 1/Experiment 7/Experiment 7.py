import timeit
import matplotlib.pyplot as plt 
import numpy as np
import math
from bad_sorts import *
from good_sorts import *

# bottom-up method of mergesort
def bottom_up_mergesort(L):
    # initializing size and length of list as variable n
    n = len(L)
    size = 1

    # consider list of length 1
    if n <= 1:
        return
    # breaking the lists up equally and building it back up
    while size < n:
        for i in range(0, n - size, 2 * size):
            # splitting the partial lists by left and right sides
            left = L[i:i + size]
            right = L[i + size:i + 2 * size]
            merged = merge(left, right)
            L[i:i + 2 * size] = merged
        # increase size of list by 2 every loop to increase the list that is sorted every time
        size *= 2

def test_allSorts(sortMethod, test_runs, increase_list):
    #initializing the list length, max value of the list and number of runs to perform for each length
    list_len = 0 
    max_value = 100
    average_runs = 100

    # lists to store the values of the x and y axis
    times = []
    list_lengths = []

    # generate random list and time the runtime
    for i in range(test_runs):
        L = create_random_list(list_len, max_value)
        time = 0

        for _ in range(average_runs):
            start = timeit.default_timer()
            sortMethod(L)
            end = timeit.default_timer()
            time += (end - start)

        # appending into the lists to plot in matplotlib
        list_lengths.append(list_len)
        times.append(time / average_runs)
        # incrementing both list length and maximum value of the list
        max_value += max_value
        list_len += increase_list

    return list_lengths, times

# run the function with both methods of mergesort
listlen1, time1 = test_allSorts(mergesort, 15, 100)
listlen2, time2 = test_allSorts(bottom_up_mergesort, 15, 100)

# sotres results of function calls into arrays
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