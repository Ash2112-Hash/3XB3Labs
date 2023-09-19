"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
"""Import the following libraries required for the sort and experiment functions"""
import random
import timeit
import matplotlib.pyplot as plot

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index




# ******************* Experiment 1 Functions *******************

# test1_InsertionSort tests the runtime of insertion sort against different and increasing list sizes (starts initially at 100)
# add more comments
def test1_InsertionSort(test_runs, average_runs, increaseList_factor):
    list_max = 100
    list_len = 100
    times = []
    list_lens = []

    for num in range(test_runs):
        L = create_random_list(list_len, list_max)
        list_lens.append(len(L))
        time_sum = 0

        for i in range(average_runs):
            start = timeit.default_timer()
            insertion_sort(L)
            end = timeit.default_timer()
            time_sum += (end-start)

        times.append(time_sum/average_runs)
        list_len += increaseList_factor
        print(times)

    plot.plot(list_lens, times, marker='o')
    plot.xlabel('List Length')
    plot.ylabel('Runtime (seconds)')
    plot.title('Insertion Sort Runtime vs List Length')
    plot.show()
    return list_lens, times


test1_InsertionSort(10, 10, 1000)