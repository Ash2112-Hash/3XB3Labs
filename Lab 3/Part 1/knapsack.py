# Knapsack Functions
import random
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

def ks_top_down(items, capacity):
    matrix = [[-1 for n in range(capacity + 1)] for m in range(len(items) + 1)]
    i = len(items)

    def knapsack(capacity, i):
        # base cases
        if i == 0 or capacity == 0:
            return 0
        if matrix[i][capacity] != -1:
            return matrix[i][capacity]   
            
        if items[i-1][0] <= capacity:
            matrix[i][capacity] = max(items[i-1][1] + knapsack(capacity - items[i-1][0], i-1), knapsack(capacity, i-1))
            return matrix[i][capacity]
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
            # filling in table with 
            elif items[value - 1][0] <= weight:
                matrix[value][weight] = max(items[value - 1][1] + matrix[value - 1][weight - items[value - 1][0]], matrix[value - 1][weight])
            # same as previous value if weight of item being checked is more than the current capacity (column)
            else:
                matrix[value][weight] = matrix[value - 1][weight]

    return matrix[len(items)][capacity]

def conduct_AverageRuns(averageRunCount, dynamic_algorithm):
    algTime_sum = 0    

    for num in range(averageRunCount):
        start_time = timeit.default_timer()    
        dynamic_algorithm            
        end_time = timeit.default_timer()      
        algTime_sum += (end_time - start_time)  
    return algTime_sum     

def test_knapsack(test_num, average_runs, increase_factor):
    numElms = 0
    valMin = 0
    weightMin = 0
    valMax = 10
    weightMax = 1000
    capacity = 100

    list_lens = []
    BU_times = []
    TD_times = []

    for num in range(test_num):
        L = createRandomTupleList(numElms, valMin, valMax, weightMin, weightMax)
        BU_sum = conduct_AverageRuns(average_runs, ks_bottom_up(L, capacity))
        TD_sum = conduct_AverageRuns(average_runs, ks_top_down(L, capacity))

        list_lens.append(len(L))
        BU_times.append(BU_sum/average_runs)
        TD_times.append(TD_sum/average_runs)

        numElms += increase_factor

    plot.plot(list_lens, BU_times, label = 'Bottom Up Approach')
    plot.plot(list_lens, TD_times, label = 'Top Down Approach')
    plot.legend(loc='upper left', title='Dynamic Programming Approach', fontsize=10)
    plot.xlabel('Number of Items (n elements)')
    plot.ylabel('Runtime (seconds)')
    plot.title("Runtime vs Number of Items")
    plot.show()

    return BU_times, TD_times

test_knapsack(5, 1, 10)


