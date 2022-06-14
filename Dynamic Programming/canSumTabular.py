def canSum(targetSum, Numbers):
    table = [False for i in range(targetSum + 2)]
    table[0] = True

    for i in range(0, targetSum + 2):
        if table[i] == True:
            for num in Numbers:
                if i + num <= targetSum + 1:
                    table[i + num] = True

    return table[targetSum]


print(canSum(10, [1, 2, 3, 5, 6, 7]))
print(canSum(7, [2, 4]))
print(canSum(7, [2, 3]))
print(canSum(300, [7, 14]))
