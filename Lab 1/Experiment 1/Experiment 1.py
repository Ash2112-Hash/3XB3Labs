# ******************* Experiment 1 Functions *******************

from bad_sorts import *

# conduct_AverageRuns conducts an average number of runs for the specific sorting algorithm and measures the corresponding runtime
def conduct_AverageRuns(averageRunCount, sortingAlgFunc, target_List):
    algTime_sum = 0

    for num in range(averageRunCount):
        start_time = timeit.default_timer()
        sortingAlgFunc(target_List)
        end_time = timeit.default_timer()
        algTime_sum += (end_time - start_time)

    return algTime_sum

# test_allSorts tests the 3 sorting algorithms for a specific amount of test_runs and plots the corresponding runtime results from each algorithm
def test_allSorts(test_runs, average_runs, increaseList_factor):
    list_max = 100
    list_len = 100
    Insertion_times = []
    Bubble_times = []
    Selection_times = []
    list_lens = []

    for num in range(test_runs):
        L = create_random_list(list_len, list_max)
        list_lens.append(len(L))
        Insertion_time_sum = conduct_AverageRuns(average_runs, insertion_sort, L)
        Bubble_time_sum = conduct_AverageRuns(average_runs, bubble_sort, L)
        Selection_time_sum = conduct_AverageRuns(average_runs, selection_sort, L)

        Insertion_times.append(Insertion_time_sum/average_runs)
        Bubble_times.append(Bubble_time_sum / average_runs)
        Selection_times.append(Selection_time_sum/ average_runs)
        list_len += increaseList_factor


    plot.plot(list_lens, Insertion_times, marker='o', label='Insertion Sort')
    plot.plot(list_lens, Selection_times, marker='o', label=' Selection Sort')
    plot.plot(list_lens, Bubble_times, marker='o', label=' Bubble Sort')
    plot.legend(loc='upper left', title='Sorting Algorithms', fontsize=12, facecolor='lightgray')
    plot.xlabel('List Length (n elements)')
    plot.ylabel('Runtime (seconds)')
    plot.title('Insertion, Bubble and Selection Sort Runtime vs List Length')
    plot.show()
    return Insertion_times, Bubble_times, Selection_times



test_allSorts(1000, 100, 1000)
