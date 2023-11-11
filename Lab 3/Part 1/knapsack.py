# Knapsack Functions
import random
import itertools


def createRandomTupleSet(numElms, valMin, valMax, weightMin, weightMax):
    rand_set = []

    for _ in range(numElms):
        rand_W = random.randint(weightMin, weightMax)
        rand_val = random.randint(valMin, valMax)

        if (rand_val, rand_W) in rand_set or (rand_W, rand_val) in rand_set:

            while True:
                NewRand_W = random.randint(weightMin, weightMax)
                NewRand_val = random.randint(valMin, valMax)

                if (rand_W, rand_val) != (NewRand_W, NewRand_val):
                    rand_set.append((NewRand_W, NewRand_val))

        rand_set.append((rand_W, rand_val))

    return rand_set



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
    i = len(items)
    j = capacity

    # base case: if j == 0 or i == 0, max = 0
    if j == 0 or i == 0:
        return 0

    elif i == 0 and j != 0:
        return -1

    else:
        if items[i - 1][0] > j:
            return ks_rec(items[:-1], j)

        else:
            return max(ks_rec(items[:-1], j), (ks_rec(items[:-1], j - items[i - 1][0]) + items[i - 1][1]))



# TODO TESTING, remove later
"""
L = [1, 2, 3]
print(L[:-1])


for i in range(20):
    items = createRandomTupleSet(10, 0, 50, 20, 50)
    result = ks_rec(items, 25)
    result2 = ks_brute_force(items, 25)
    print("Maximum value:", result)
    print("Maximum value:", result2)
    assert result == result2


items = createRandomTupleSet(10, 0, 50, 20, 50)
result = ks_rec(items, 25)
print("Maximum value:", result)
result2 = ks_brute_force(items, 25)
print("Maximum value:", result2)
"""
