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
            for k in range(len(L)):
                print(L[k])
        L[j + 1] = placeholder

# ******Bubble sort******

def bubble_sort2(L):
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
        for num in L:
            print(num)
        print("next")

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

def main():
    L = [1, 2, 5, 7, 4, 9, 3, 6, 8]
    #insertion_sort2(L)
    bubble_sort2(L)
    #selection_sort2(L)

main()