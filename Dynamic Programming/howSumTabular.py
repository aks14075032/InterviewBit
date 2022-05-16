def howSum(targetSum, Numbers):
    table = [None for i in range(targetSum+2)]
    table[0]=[]

    for i in range(0,targetSum+2):
        if table[i] != None:
            for num in Numbers:
                if i + num <= targetSum+1:
                    table[i+num] = []
                    table[i+num] = table[i+num] + table[i]
                    table[i+num].append(num)

    return table[targetSum]

print(howSum(10,[1,2,3,5,6,7]))
print(howSum(7,[2,4])) 
print(howSum(7,[2,3]))
print(howSum(300,[7,14]))