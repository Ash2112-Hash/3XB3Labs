# ******************* Experiment 1 Functions *******************

from bad_sorts import *


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
        Insertion_time_sum = 0
        Bubble_time_sum = 0
        Selection_time_sum = 0

        for i in range(average_runs):
            start_1 = timeit.default_timer()
            insertion_sort(L)
            end_1 = timeit.default_timer()
            Insertion_time_sum += (end_1-start_1)

            start_2 = timeit.default_timer()
            bubble_sort(L)
            end_2 = timeit.default_timer()
            Bubble_time_sum += (end_2 - start_2)

            start_3 = timeit.default_timer()
            selection_sort(L)
            end_3 = timeit.default_timer()
            Selection_time_sum += (end_3 - start_3)

        Insertion_times.append(Insertion_time_sum/average_runs)
        Bubble_times.append(Bubble_time_sum / average_runs)
        Selection_times.append(Selection_time_sum/ average_runs)
        list_len += increaseList_factor
        #print(times)

    plot.plot(list_lens, Insertion_times, marker='o')
    plot.plot(list_lens, Selection_times, marker='o')
    plot.plot(list_lens, Bubble_times, marker='o')
    plot.xlabel('List Length')
    plot.ylabel('Runtime (seconds)')
    plot.title('Insertion, Bubble and Selection Sort Runtime vs List Length')
    plot.show()
    return None



test_allSorts(10, 10, 50)
