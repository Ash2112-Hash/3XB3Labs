""" Experiment 1:
Functions and cases to test and compare brute force and recursive knapsack solutions.
"""

import random


def createRandomSet(numElms, weightMin, weightMax):
    rand_set = set()

    if numElms >= weightMax:
        numElms = weightMax

    for _ in range(numElms):
        rand_elm = random.randint(weightMin, weightMax)

        while rand_elm in rand_set:
            newRand_elm = random.randint(weightMin, weightMax)

            if rand_elm != newRand_elm and newRand_elm not in rand_set:
                rand_elm = newRand_elm
                break

        rand_set.add(rand_elm)

    return rand_set

def plotExp1Results():
    pass
