import good_sorts
import bad_sorts
import matplotlib.pyplot as plt
import timeit

def test_allSorts(test_runs, average_runs, increaseList_factor):
    list_max = 100
    list_len = 100
    Quick_times = []
    Merge_times = []
    Heap_times = []
    list_lens = []

    for i in range(test_runs):
        L = bad_sorts.create_random_list(list_len, list_max)
        list_lens.append(len(L))
        Quick_time_sum = 0
        Merge_time_sum = 0
        Heap_time_sum = 0

        for run in range(average_runs): #running multiple tests for accuracy
            start_1 = timeit.default_timer()
            good_sorts.quicksort(L.copy())
            end_1 = timeit.default_timer()
            Quick_time_sum += (end_1-start_1)

            start_2 = timeit.default_timer()
            good_sorts.mergesort(L.copy())
            end_2 = timeit.default_timer()
            Merge_time_sum += (end_2 - start_2)

            start_3 = timeit.default_timer()
            good_sorts.heapsort(L.copy())
            end_3 = timeit.default_timer()
            Heap_time_sum += (end_3 - start_3)

        Quick_times.append(Quick_time_sum/average_runs)
        Merge_times.append(Merge_time_sum / average_runs)
        Heap_times.append(Heap_time_sum/ average_runs)
        list_len += increaseList_factor
        list_max += increaseList_factor
        #print(times)

    #plotting the graph
    plt.plot(list_lens, Quick_times, marker='o')
    plt.plot(list_lens, Merge_times, marker='o')
    plt.plot(list_lens, Heap_times, marker='o')
    plt.xlabel('List Length')
    plt.ylabel('Runtime (seconds)')
    plt.title('Good Sorts vs List Length')
    plt.legend(['Quick Sort', 'Merge Sort', 'Heap Sort'])
    plt.show()
    return None

def main():
    test_allSorts(15, 30, 100)

main()