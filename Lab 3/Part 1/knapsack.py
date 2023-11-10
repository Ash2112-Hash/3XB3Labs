# Knapsack Functions
import random
import itertools
import timeit
import matplotlib.pyplot as plot

def createRandomTupleList(numElms, valMin, valMax, weightMin, weightMax):
    rand_list = []

    for _ in range(numElms):
        rand_W = random.randint(weightMin, weightMax)
        rand_val = random.randint(valMin, valMax)
        
        if (rand_val, rand_W) in rand_list or (rand_W, rand_val) in rand_list:

            while True:
                NewRand_W = random.randint(weightMin, weightMax)
                NewRand_val = random.randint(valMin, valMax)

                if (rand_W, rand_val) != (NewRand_W, NewRand_val):
                    rand_list.append((NewRand_W, NewRand_val))

        rand_list.append((rand_W, rand_val))

    return rand_list

def ks_brute_force(items, capacity):
    max_val = 0
    initial_subsets = []
    item_subsets = []

    for i in range(len(items) + 1):
        initial_subsets.extend(itertools.combinations(items, i))

    for each_subset in initial_subsets:
        item_subsets.append(list(each_subset))

    for each_subset in item_subsets:
        new_W = sum(item_tuple[0] for item_tuple in each_subset)
        new_value = sum(item_tuple[1] for item_tuple in each_subset)

        if new_W <= capacity and new_value > max_val:
            max_val = new_value

    return max_val

def ks_rec(items, capacity):
    max_val = 0
    i = len(items)
    j = capacity

    # base case: if j == 0
    if capacity == 0 or len(items) == 0:
        return 0

    # base case: if j < 0, return -1 as indicator for N/A, not possible for capacity for < 0
    elif capacity < 0:
        return -1

    # base case: if i == 0, max_val will never > 0
    elif len(items) == 0:
        return max_val

    else:
        if items[i - 1][0] > j:
            return ks_rec(items[:-1], j)

        else:
            return max(ks_rec(items[:-1], j), ks_rec(items[:-1], j - items[i - 1][0]) + items[i - 1][1])

def ks_top_down(items, capacity):
    matrix = [[-1 for n in range(capacity + 1)] for m in range(len(items) + 1)]
    i = len(items)

    def knapsack(capacity, i):
        # base cases
        if i == 0 or capacity == 0:
            return 0
        if matrix[i][capacity] != -1:
            return matrix[i][capacity]   
        # returning value of current item if previous item's weight that is less the capacity
        if items[i-1][0] <= capacity:
            matrix[i][capacity] = max(items[i-1][1] + knapsack(capacity - items[i-1][0], i-1), knapsack(capacity, i-1))
            return matrix[i][capacity]
        # returning value of current item if previous item's weight that is more the capacity
        else:
            matrix[i][capacity] = knapsack(capacity, i-1)
            return matrix[i][capacity]
    return knapsack(capacity, i)

def ks_bottom_up(items, capacity):
    # create matrix from 0 to capacity for columns and 0 to length of item list for rows
    matrix = [[0 for j in range(capacity + 1)] for i in range(len(items) + 1)]
    
    for value in range(len(items) + 1):
        for weight in range(capacity + 1):
            # base cases (when there is no weight or value, the profit is 0)
            if value == 0 or weight == 0:
                matrix[value][weight] = 0
            # filling in table for items that have previous weights that are less the current capacity
            elif items[value - 1][0] <= weight:
                matrix[value][weight] = max(items[value - 1][1] + matrix[value - 1][weight - items[value - 1][0]], matrix[value - 1][weight])
            # same as previous value if weight of item being checked is more than the current capacity (column)
            else:
                matrix[value][weight] = matrix[value - 1][weight]

    return matrix[len(items)][capacity]

def TDvsBU(average_runs):
    capacity = 50
    valMin, weightMin = 0, 0
    valMax, weightMax = 100, 100

    list_lens = [n for n in range(1, 700)]
    BU_times = []
    TD_times = []

    for n in list_lens:
        BU_sum, TD_sum = 0, 0

        for _ in range(average_runs):
            items = createRandomTupleList(n, valMin, valMax, weightMin, weightMax)
            
            start_time = timeit.default_timer()
            BU = ks_bottom_up(items, capacity)
            end_time = timeit.default_timer()
            BU_sum += (end_time - start_time)  

            start_time = timeit.default_timer()
            TD = ks_top_down(items, capacity)
            end_time = timeit.default_timer()
            TD_sum += (end_time - start_time)

        BU_times.append(BU_sum/average_runs)
        TD_times.append(TD_sum/average_runs)  

    plot.plot(list_lens, BU_times, label = 'Bottom Up Approach')
    plot.plot(list_lens, TD_times, label = 'Top Down Approach')
    plot.legend(loc = 'upper left', title = 'Dynamic Programming Approach', fontsize=10)
    plot.xlabel('Number of Items (n elements)')
    plot.ylabel('Runtime (seconds)')
    plot.title("Runtime vs Number of Items")
    plot.show()

def BUvsTD(average_runs):
    capacity = 50
    valMin, weightMin = 0, 0
    valMax, weightMax = 2000, 2000

    list_lens = [n for n in range(1, 500)]
    BU_times = []
    TD_times = []

    for n in list_lens:
        BU_sum, TD_sum = 0, 0

        for _ in range(average_runs):
            items = createRandomTupleList(n, valMin, valMax, weightMin, weightMax)
            
            start_time = timeit.default_timer()
            BU = ks_bottom_up(items, capacity)
            end_time = timeit.default_timer()
            BU_sum += (end_time - start_time)  

            start_time = timeit.default_timer()
            TD = ks_top_down(items, capacity)
            end_time = timeit.default_timer()
            TD_sum += (end_time - start_time)
            assert BU == TD

        BU_times.append(BU_sum/average_runs)
        TD_times.append(TD_sum/average_runs)  

    plot.plot(list_lens, BU_times, label = 'Bottom Up Approach')
    plot.plot(list_lens, TD_times, label = 'Top Down Approach')
    plot.legend(loc = 'upper left', title = 'Dynamic Programming Approach', fontsize=10)
    plot.xlabel('Number of Items (n elements)')
    plot.ylabel('Runtime (seconds)')
    plot.title("Runtime vs Number of Items")
    plot.show()

# TODO TESTING, remove later
""" 
for i in range(20):
    items = createRandomTupleSet(10, 0, 50, 20, 50)
    result = ks_rec(items, 25)
    result2 = ks_brute_force(items, 25)
    assert result == result2
    print("Maximum value:", result)
    print("Maximum value:", result2)


items = createRandomTupleSet(10, 0, 50, 20, 50)
result = ks_rec(items, 25)
print("Maximum value:", result)
result2 = ks_brute_force(items, 25)
print("Maximum value:", result2)
"""
