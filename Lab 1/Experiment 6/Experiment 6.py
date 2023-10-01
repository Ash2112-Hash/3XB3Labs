# ******************* Experiment 6 Functions *******************
# Functions designated to running experiment 6 pertaining to verifying a potential speedup of quick sort

# TODO maybe add partially sorted and sorted lists to test as well

# Import the necessary modules/libraries needed for experiment
from good_sorts import quicksort
from bad_sorts import create_random_list
import timeit
import matplotlib.pyplot as plot


# conduct_AverageRuns conducts an average number of runs for the specific sorting algorithm and measures the corresponding runtime of the algorithm (aginest a target list)
# Paramaters: averageRunCount (number of average runs),  sortingAlgFunc (specific sorting algorithm function) and target_List(specific list to be used)
def conduct_AverageRuns(averageRunCount, sortingAlgFunc, target_List):
    algTime_sum = 0     #sum variable to store sum of runtime for the sorting alg

    # iterates over a specified amount of runs and obtain a average runtime for the sorting algorithm
    for num in range(averageRunCount):
        start_time = timeit.default_timer()     # starts the timer
        sortingAlgFunc(target_List.copy())             # calls the sort alg function with a copy of the list
        end_time = timeit.default_timer()       # ends the time
        algTime_sum += (end_time - start_time)  # adds the runtime to the algTime_sum

    return algTime_sum      # returns the sum of the average runtimes


# dual_quicksort(L) sorts a list using two pivots (first and second elements of the list respectively) via recursion
def dual_quicksort(L):
    if len(L) < 3:      # base case needed for dual quicksort, if len < 3, return the list
        return L

    # assign first and second pivot to first and second elements of L respectively
    first_pivot = L[0]
    sec_pivot = L[1]
    left, middle, right = [], [], []        #create lists to store the left, right and mid portions of the L during recursion sorting

    # if first pivot is greater than second pivot, swap them within L
    if(first_pivot > sec_pivot):
        first_pivot = L[1]
        sec_pivot = L[0]

    # iterate through all numbers from index 2 of L to its end
    for num in L[2:]:
        if num < first_pivot:       # if num is less than first_pivot, add it to left portion
            left.append(num)

        elif num > sec_pivot:       # if num is greater than sec_pivot, add it to right portion
            right.append(num)

        else:                       # if num <= first pivor and num <= sec_pivot, add it to middle portion
            middle.append(num)

    return dual_quicksort(left) + [first_pivot] + dual_quicksort(middle) + [sec_pivot] + dual_quicksort(right)
    # recursively sort the portions and return them in the corresponding order as final sorted L


# DualvsSingle_QuickSort tests dual quicksort vs. normal quicksort for a specific amount of test_runs and plots the corresponding runtime results from each algorithm using matplotlib
# Paramaters: test_runs(number of actual test runs), average_runs (number of average runs - done during each actual test run) and increaseList_factor(factor used to increase the list size)
def DualvsSingle_QuickSort(test_runs, average_runs, increaseList_factor):
    list_max = 100
    list_len = 0
    # declare the default max and len of list: 0

    # lists to store the average runtimes computed for each sorting alg as well as the increasing lengths of the list
    SingleQuick_times = []
    DualQuick_times = []
    list_lens = []

    # iterates over the specified number of test runs, creates a new list in each run and conducts average runs for dual quicksort and normal quicksort
    for num in range(test_runs):
        L = create_random_list(list_len, list_max)
        SingleQuick_time_sum = conduct_AverageRuns(average_runs, quicksort, L)
        DualQuick_time_sum = conduct_AverageRuns(average_runs, dual_quicksort, L)

        # appends the target list length and runtimes of the sorting algs to the corresponding time lusts
        list_lens.append(len(L))
        SingleQuick_times.append(SingleQuick_time_sum/average_runs)
        DualQuick_times.append(DualQuick_time_sum/ average_runs)

        # increases the list's length by a corresponding factor
        list_len += increaseList_factor
        list_max += increaseList_factor


    # plots the runtimes of the 3 sorting algorithms with the following legends and axis titles
    plot.plot(list_lens, SingleQuick_times, label='Single Pivot QuickSort')
    plot.plot(list_lens, DualQuick_times, label='Dual Pivot Quicksort')
    plot.legend(loc='upper left', title='Quicksort Algorithms', fontsize=10, facecolor='lightgray')
    plot.xlabel('List Length (n elements)')
    plot.ylabel('Runtime (seconds)')
    plot.title("Dual and Single Quicksort's Runtime vs. List Length")
    plot.show()

    # returns the accumulated runtimes of all the sorting algs
    return SingleQuick_times, DualQuick_times


# assertions used to test the validity of the dual_quicksort alg against the normal quicksort
L = create_random_list(100, 100)
L2 = create_random_list(1000, 10000)
L3 = create_random_list(1000, 10000)
L4 = create_random_list(1000, 70000)
assert(quicksort(L) == dual_quicksort(L))
assert(quicksort(L2) == dual_quicksort(L2))
assert(quicksort(L3) == dual_quicksort(L3))
assert(quicksort(L4) == dual_quicksort(L4))



# calls the function to commence the test and plot the curve with the following parameters: 15 test runs, 30 average runs (for each test run) with an increasing list factor of 100
DualvsSingle_QuickSort(25, 30, 100)



