import timeit
import matplotlib.pyplot as plt 
import numpy as np
import math
from bad_sorts import *

def test_allSorts(sortType):
    # chosen number of list length, max values of list, swaps and average runs
    list_len = 1000
    max_value = 100
    average_runs = 25
    num_swaps = int(list_len*math.log(list_len,10)/2)

    # lists to store the times and number of swaps performed for each sorting algorithm
    times = []
    swaps = []

    # restarts the timer for every sorting algorithm
    for i in range(0, num_swaps, 100):
        time = 0

        # running the experiment multiple times to obtain an accurate estimate
        for _ in range(average_runs):
            L = create_near_sorted_list(list_len, max_value, i)
            start = timeit.default_timer()
            sortType(L)
            end = timeit.default_timer()
            time += (end - start)
        swaps.append(i)
        times.append(time / average_runs)
        # incrementing by itself to avoid duplicates from randomized list
        max_value += max_value

    #returns x and y axis
    return swaps, times

# calls the function for the runtimes of the 3 sorting algorithms 
swaps1, time1 = test_allSorts(insertion_sort)
swaps2, time2 = test_allSorts(bubble_sort)
swaps3, time3 = test_allSorts(selection_sort)

# stores the results of the function calls in an array to display the data
swap_insertion, time_insertion = np.array(swaps1), np.array(time1)
swap_bubble, time_bubble = np.array(swaps2), np.array(time2)
swap_selection, time_selection = np.array(swaps3), np.array(time3)

# plotting the data and establishing the graph labels
plt.title("Number of Swaps vs Runtime")
plt.xlabel("Number of Swaps")
plt.ylabel("Runtime (seconds)")
plt.plot(swap_insertion, time_insertion, color = 'r', label = 'Insertion Sort')
plt.plot(swap_bubble, time_bubble, color = 'b', label = 'Bubble Sort')
plt.plot(swap_selection, time_selection, color = 'g', label = 'Selection Sort')
plt.legend()
plt.show()