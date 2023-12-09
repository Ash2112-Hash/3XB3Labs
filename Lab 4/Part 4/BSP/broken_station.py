def bsp_value(L, m):
    if len(L) == 0:
        return 0

    #initializing
    table = [[float('inf') for j in range(m+1)] for i in range(len(L)+1)]

    table[2][0] = L[1] - L[0]

    for i in range(3, len(L) + 1):
        for j in range(m+1):
            maxmin = - 1
            for k in range(j+1):
                maxmin = max(min(table[i - 1 - k][j - k], L[i-1] - L[i-2-k]), maxmin)
            table[i][j] = maxmin
        
    return table[len(L)][m]

def bsp_solution(L, m):

    #initializing
    table = [[float('inf') for j in range(m+1)] for i in range(len(L)+1)]
    solution = [[[] for j in range(m+1)] for i in range(len(L) + 1)]

    table[2][0] = L[1] - L[0]
    solution[2][0] = [L[0], L[1]]

    for i in range(3, len(L) + 1):
        for j in range(m+1):
            maxmin = -1
            solved = []

            for k in range(j+1):
                current = min(table[i-1-k][j-k], L[i-1]-L[i-2-k])
                if current > maxmin:
                    maxmin = current
                    solved = solution[i-1-k][j-k] + [L[i-1]]

            table[i][j] = maxmin
            solution[i][j] = solved

    if len(solution[len(L)][m]) != len(L) - m:
        return [L[0]] + solution[len(L)][m]
    
    return solution[len(L)][m]

print(bsp_value([2, 4, 6, 7, 10, 14], 2))
print(bsp_solution([2, 4, 6, 7, 10, 14], 2))