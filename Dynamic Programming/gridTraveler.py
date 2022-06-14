def gridTraveler(m, n):
    grid = [[0 for i in range(n + 1)] for j in range(m + 1)]
    grid[1][1] = 1
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            temp = grid[i][j]
            if i + 1 <= m:
                grid[i + 1][j] = grid[i + 1][j] + temp
            if j + 1 <= n:
                grid[i][j + 1] = grid[i][j + 1] + temp
    return grid[m][n]


print(gridTraveler(1, 1))
print(gridTraveler(2, 3))
print(gridTraveler(3, 2))
print(gridTraveler(3, 3))
print(gridTraveler(18, 18))
