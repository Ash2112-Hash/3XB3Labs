# ******************* Experiment 8 Functions *******************
# Functions designated to running experiment 8 pertaining to compare insertion sort to merge and quick sort for small list sizes.


# Import the necessary modules/libraries needed for experiment
from good_sorts import quicksort, mergesort
from bad_sorts import create_random_list, insertion_sort
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



# test_allSorts tests the 3 sorting algorithms for a specific amount of test_runs and plots the corresponding runtime results from each algorithm using matplotlib
# Paramaters: test_runs(number of actual test runs), average_runs (number of average runs - done during each actual test run) and increaseList_factor(factor used to increase the list size)
def test_allSorts(test_runs, average_runs, increaseList_factor):
    list_max = 0
    list_len = 0
    # declare the default max and len of list: 0

    # lists to store the average runtimes computed for each sorting alg as well as the increasing lengths of the list
    Insertion_times = []
    QuickSort_times = []
    MergeSort_times = []
    list_lens = []

    # iterates over the specified number of test runs, creates a new list in each run and conducts average runs for each of the 3 sorting algorithms against the list (in each iteration)
    for num in range(test_runs):
        L = create_random_list(list_len, list_max)
        Insertion_time_sum = conduct_AverageRuns(average_runs, insertion_sort, L)
        QuickSort_time_sum = conduct_AverageRuns(average_runs, quicksort, L)
        MergeSort_time_sum = conduct_AverageRuns(average_runs, mergesort, L)

        # appends the target list length and runtimes of the sorting algs to the corresponding time lusts
        list_lens.append(len(L))
        Insertion_times.append(Insertion_time_sum/average_runs)
        QuickSort_times.append(QuickSort_time_sum / average_runs)
        MergeSort_times.append(MergeSort_time_sum/ average_runs)

        # increases the list's length by a corresponding factor
        list_len += increaseList_factor
        list_max += increaseList_factor


    # plots the runtimes of the 3 sorting algorithms with the following legends and axis titles
    plot.plot(list_lens, Insertion_times, label='Insertion Sort')
    plot.plot(list_lens, MergeSort_times, label='Merge Sort')
    plot.plot(list_lens, QuickSort_times, label='Quick Sort')
    plot.legend(loc='upper left', title='Sorting Algorithms', fontsize=10)
    plot.xlabel('List Length (n elements)')
    plot.ylabel('Runtime (seconds)')
    plot.title("Good vs. Bad Sorting Algorithms on Smaller List Sizes")
    plot.show()

    # returns the accumulated runtimes of all the sorting algs
    return Insertion_times, QuickSort_times, MergeSort_times


# Pic 1 to show where Insertion sort is good and transitions to become inefficient
# calls the function to commence the test and plot the curve with the following parameters: 13 test runs, 30 average runs (for each test run) with an increasing list factor of 1 (focusing mainly on insertion vs quick sort in this case)
test_allSorts(13, 30, 1)

# Pic 2 to show where Insertion sort becomes inefficient
# calls the function to commence the test and plot the curve with the following parameters: 15 test runs, 30 average runs (for each test run) with an increasing list factor of 1 (merge vs insertion in this case)
test_allSorts(100, 30, 1)
