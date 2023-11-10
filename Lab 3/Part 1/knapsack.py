# Knapsack Functions
import random
import timeit
import matplotlib.pyplot as plot

def createRandomTupleList(numElms, valMin, valMax, weightMin, weightMax):
    rand_list = []

    for _ in range(numElms):
        rand_W = random.randint(weightMin, weightMax)
        rand_val = random.randint(valMin, valMax)
        rand_list.append((rand_W, rand_val))

    return rand_list

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

        BU_times.append(BU_sum/average_runs)
        TD_times.append(TD_sum/average_runs)  

    plot.plot(list_lens, BU_times, label = 'Bottom Up Approach')
    plot.plot(list_lens, TD_times, label = 'Top Down Approach')
    plot.legend(loc = 'upper left', title = 'Dynamic Programming Approach', fontsize=10)
    plot.xlabel('Number of Items (n elements)')
    plot.ylabel('Runtime (seconds)')
    plot.title("Runtime vs Number of Items")
    plot.show()