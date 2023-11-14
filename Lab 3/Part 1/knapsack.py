# Knapsack Functions
import random
import itertools


# function to generate and return a random set of item tuples
# parameters: number of items, minimum/maximum value and minimum/maximum weight
def createRandomTupleList(numElms, valMin, valMax, weightMin, weightMax):
    rand_list = []

    for _ in range(numElms):
        rand_W = random.randint(weightMin, weightMax)
        rand_val = random.randint(valMin, valMax)
        # generates the random weight and value for items
        
        if (rand_val, rand_W) in rand_list or (rand_W, rand_val) in rand_list:
            # verifies the item is not already within the list
            # if already in list, generate a new value and weight to store within list

            while True:
                NewRand_W = random.randint(weightMin, weightMax)
                NewRand_val = random.randint(valMin, valMax)

                if (rand_W, rand_val) != (NewRand_W, NewRand_val):
                    rand_list.append((NewRand_W, NewRand_val))

        rand_list.append((rand_W, rand_val))

    return rand_list
    # return the random item list


# function to solve the knapsack problem by brute force
# parameters: items list and capacity
def ks_brute_force(items, capacity):
    max_val = 0
    initial_subsets = []
    item_subsets = []

    # generates and stores all possible subsets of the items list into initial_subsets list
    for i in range(len(items) + 1):
        initial_subsets.extend(itertools.combinations(items, i))

    # casts each subset to a list and adds it within item_subsets list for easier access/traversal for next loop
    for each_subset in initial_subsets:
        item_subsets.append(list(each_subset))

    # sums up the weight and value of each subset and returns the maximum value of the subset that does not exceed capacity
    for each_subset in item_subsets:
        new_W = sum(item_tuple[0] for item_tuple in each_subset)
        new_value = sum(item_tuple[1] for item_tuple in each_subset)

        if new_W <= capacity and new_value > max_val:
            max_val = new_value

    return max_val


# function to solve the knapsack problem by recursion (without dynammic programming)
# parameters: items list and capacity
def ks_rec(items, capacity):
    i = len(items)
    j = capacity

    # base cases: if j == 0 or i == 0, return a max = 0
    if j == 0 or i == 0:
        return 0

    # otherwise, consider the following conditions
    else:
        # if item's weight exceeds capacity, exclude it and look at remaining items
        if items[i - 1][0] > j:
            return ks_rec(items[:-1], j)

        # if item's weight is <= capacity, return the max between excluding it and including it within the bag
        else:
            return max(ks_rec(items[:-1], j), (ks_rec(items[:-1], j - items[i - 1][0]) + items[i - 1][1]))


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


