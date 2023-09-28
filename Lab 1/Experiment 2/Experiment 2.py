import bad_sorts
import matplotlib.pyplot as plt
import timeit

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ******Insertion sort******

def insertion_sort2(L):
    for i in range(1, len(L)): 
        placeholder = L[i]
        j = i - 1
        while j >= 0 and placeholder < L[j]:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = placeholder

# ******Bubble sort******

def bubble_sort2(L): #this one works fine
    for i in range(len(L)):
        swapped = False
        for j in range(0, len(L)-i-1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                swapped = True
        if not swapped:
            break

# ******Selection sort******

def selection_sort2(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        max_index = find_max_index(L, i)
        swap(L, i, min_index)
        swap(L, i, max_index)

def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

def find_max_index(L, m):
    max_index = m
    for i in range(len(L)):
        if L[i] > L[max_index]:
            max_index = i
    return max_index

def test_allSorts(test_runs, average_runs, increaseList_factor):
    list_max = 100
    list_len = 100
    Insertion_times = []
    Bubble_times = []
    Selection_times = []
    Insertion2_times = []
    Bubble2_times = []
    Selection2_times = []
    list_lens = []

    for i in range(test_runs):
        L = bad_sorts.create_random_list(list_len, list_max)
        list_lens.append(len(L))
        Insertion_time_sum = 0
        Insertion_L = L.copy()
        Bubble_time_sum = 0
        Bubble_L = L.copy()
        Selection_time_sum = 0
        Selection_L = L.copy()
        Insertion2_time_sum = 0
        Insertion2_L = L.copy()
        Bubble2_time_sum = 0
        Bubble2_L = L.copy()
        Selection2_time_sum = 0
        Selection2_L = L.copy()

        for i in range(average_runs):
            start_1 = timeit.default_timer()
            bad_sorts.insertion_sort(Insertion_L)
            end_1 = timeit.default_timer()
            Insertion_time_sum += (end_1-start_1)

            start_2 = timeit.default_timer()
            bad_sorts.bubble_sort(Bubble_L)
            end_2 = timeit.default_timer()
            Bubble_time_sum += (end_2 - start_2)

            start_3 = timeit.default_timer()
            bad_sorts.selection_sort(Selection_L)
            end_3 = timeit.default_timer()
            Selection_time_sum += (end_3 - start_3)

            start4 = timeit.default_timer()
            selection_sort2(Selection2_L)
            end_4 = timeit.default_timer()
            Insertion2_time_sum += (end_4 - start4)

            start_5 = timeit.default_timer()
            bubble_sort2(Bubble2_L)
            end_5 = timeit.default_timer()
            Bubble2_time_sum += (end_5 - start_5)

            start_6 = timeit.default_timer()
            selection_sort2(Selection2_L)
            end_6 = timeit.default_timer()
            Selection2_time_sum += (end_6 - start_6)

        Insertion_times.append(Insertion_time_sum/average_runs)
        Bubble_times.append(Bubble_time_sum / average_runs)
        Selection_times.append(Selection_time_sum/ average_runs)
        Insertion2_times.append(Insertion2_time_sum/average_runs)
        Bubble2_times.append(Bubble2_time_sum / average_runs)
        Selection2_times.append(Selection2_time_sum/ average_runs)
        list_len += increaseList_factor
        #print(times)

    plt.plot(list_lens, Insertion_times, marker='o')
    plt.plot(list_lens, Selection_times, marker='o')
    plt.plot(list_lens, Bubble_times, marker='o')
    plt.plot(list_lens, Insertion2_times, marker='o')
    plt.plot(list_lens, Selection2_times, marker='o')
    plt.plot(list_lens, Bubble2_times, marker='o')
    plt.xlabel('List Length')
    plt.ylabel('Runtime (seconds)')
    plt.title('Bad Sorts (with Their Improvements) vs List Length')
    plt.legend(['Insertion Sort', 'Selection Sort', 'Bubble Sort', 'Insertion Sort 2', 'Selection Sort 2', 'Bubble Sort 2'])
    plt.show()
    return None

def main():
    test_allSorts(10, 10, 50)

main()