

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