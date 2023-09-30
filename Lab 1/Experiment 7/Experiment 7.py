import timeit
import matplotlib.pyplot as plt 
import numpy as np
import math
from bad_sorts import *
from good_sorts import *

L = create_random_list(20,100)

def bottom_up_mergesort(L):
    n = len(L)
    size = 1

    if n <= 1:
        return
    
    while size < n:
        for i in range(0, n, 2 * size):
            left = L[i:i + size]
            right = L[i + size:i + 2 * size]
            merged = merge(left, right)
            L[i:i + 2 * size] = merged
        size *= 2

def test_allSorts(firstSort, secondSort):
    times = []
    swaps = []

    for i in range(0, num_swaps, 100):
        time = 0

        for _ in range(20):
            L = create_near_sorted_list(1000, 100, i)
            start = timeit.default_timer()
            end = timeit.default_timer()
            time += (end - start)
        swaps.append(i)
        times.append(time / 20)

    return swaps, times