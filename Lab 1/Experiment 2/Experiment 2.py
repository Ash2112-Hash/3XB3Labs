import bad_sorts
import matplotlib.pyplot as plt
import timeit

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ******Insertion sort 2******

def insertion_sort2(L):
    for i in range(1, len(L)): 
        placeholder = L[i]
        j = i
        while j > 0 and L[j - 1] > placeholder:
            L[j] = L[j - 1] #shifts up instead of down
            j -= 1
        L[j] = placeholder

# ******Bubble sort 2******

def bubble_sort2(L):
    for i in range(len(L)):
        swapped = False
        for j in range(0, len(L)-i-1):
            if L[j] > L[j+1]:
                swap(L, j, j+1) #shifts up instead of down
                swapped = True
        if not swapped:
            break

# ******Selection sort 2******

def selection_sort2(L):
    i = 0
    j = len(L) - 1
    while (i < j):
        minimum = L[i]
        maximum = L[i]
        min_index = i
        max_index = i
        for k in range(i, j+1):
            if (L[k] > maximum):
                maximum = L[k]
                max_index = k
            elif (L[k] < minimum):
                minimum = L[k]
                min_index = k

        swap(L, i, k)

        if (L[min_index] == maximum):
            swap(L, j, min_index)
        else:
            swap(L, j, max_index) #this is the added "max" swap

        i += 1
        j -= 1

# ******Graphing*******

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
        Bubble_time_sum = 0
        Selection_time_sum = 0
        Insertion2_time_sum = 0
        Bubble2_time_sum = 0
        Selection2_time_sum = 0

        for i in range(average_runs): #running the experiment multiple times for more accuracy
            start_1 = timeit.default_timer()
            bad_sorts.insertion_sort(L.copy())
            end_1 = timeit.default_timer()
            Insertion_time_sum += (end_1-start_1)

            start_2 = timeit.default_timer()
            bad_sorts.bubble_sort(L.copy())
            end_2 = timeit.default_timer()
            Bubble_time_sum += (end_2 - start_2)

            start_3 = timeit.default_timer()
            bad_sorts.selection_sort(L.copy())
            end_3 = timeit.default_timer()
            Selection_time_sum += (end_3 - start_3)

            start4 = timeit.default_timer()
            insertion_sort2(L.copy())
            end_4 = timeit.default_timer()
            Insertion2_time_sum += (end_4 - start4)

            start_5 = timeit.default_timer()
            bubble_sort2(L.copy())
            end_5 = timeit.default_timer()
            Bubble2_time_sum += (end_5 - start_5)

            start_6 = timeit.default_timer()
            selection_sort2(L.copy())
            end_6 = timeit.default_timer()
            Selection2_time_sum += (end_6 - start_6)

        Insertion_times.append(Insertion_time_sum/average_runs)
        Bubble_times.append(Bubble_time_sum / average_runs)
        Selection_times.append(Selection_time_sum/ average_runs)
        Insertion2_times.append(Insertion2_time_sum/average_runs)
        Bubble2_times.append(Bubble2_time_sum / average_runs)
        Selection2_times.append(Selection2_time_sum/ average_runs)
        list_len += increaseList_factor
        list_max += increaseList_factor

    #plotting the graph
    plt.plot(list_lens, Insertion_times, marker='o')
    plt.plot(list_lens, Bubble_times, marker='o')
    plt.plot(list_lens, Selection_times, marker='o')
    plt.plot(list_lens, Insertion2_times, marker='o')
    plt.plot(list_lens, Bubble2_times, marker='o')
    plt.plot(list_lens, Selection2_times, marker='o')
    plt.xlabel('List Length')
    plt.ylabel('Runtime (seconds)')
    plt.title('Bad Sorts (with Their Improvements) vs List Length')
    plt.legend(['Insertion Sort', 'Bubble Sort', 'Selection Sort', 'Insertion Sort 2', 'Bubble Sort 2', 'Selection Sort 2'])
    plt.show()
    return None

def main():
    test_allSorts(15, 30, 100)

main()