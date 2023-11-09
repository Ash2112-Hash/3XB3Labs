def ks_bottom_up(items, capacity):
    # create matrix from 0 to capacity for columns and 0 to length of item list for rows
    matrix = [[0 for j in range(capacity + 1)] for i in range(len(items) + 1)]
    
    for value in range(len(items) + 1):
        for weight in range(capacity + 1):
            # base cases (when there is no weight or value, the profit is 0)
            if value == 0 or weight == 0:
                matrix[value][weight] = 0
            elif items[value - 1][0] <= weight:
                matrix[value][weight] = max(items[value - 1][1] + matrix[value - 1][weight - items[value - 1][0]], matrix[value - 1][weight])
            else:
                matrix[value][weight] = matrix[value - 1][weight]

    return matrix[len(items)][capacity]
