# Knapsack Functions
import random



def createRandomTupleSet(numElms, valMin, valMax, weightMin, weightMax):
    rand_set = set()

    for _ in range(numElms):
        rand_W = random.randint(weightMin, weightMax)
        rand_val = random.randint(valMin, valMax)

        if (rand_val, rand_W) in rand_set or (rand_W, rand_val) in rand_set:

            while True:
                NewRand_W = random.randint(weightMin, weightMax)
                NewRand_val = random.randint(valMin, valMax)

                if (rand_val, rand_W) != (NewRand_val, NewRand_W):
                    rand_set.add((NewRand_val, NewRand_W))

        rand_set.add((rand_W, rand_val))

    return rand_set




def ks_brute_force(items, capacity):
    pass



