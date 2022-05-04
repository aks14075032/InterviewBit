#Solution is not working need to rethink on it


def bestSum(targetSum, numbers, memo=None):

    if memo is None:
        memo = {}
    
    if targetSum in memo:
        return memo[targetSum]
    if targetSum < 0: return None
    if targetSum == 0: return []
    
    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination is not None:
            remainderCombination.append(num)
            memo[targetSum] = remainderCombination
            if shortestCombination == None or len(shortestCombination) > len(remainderCombination):
                shortestCombination = remainderCombination
                memo[targetSum] = shortestCombination

    memo[targetSum] = shortestCombination
    return shortestCombination


# print(bestSum(10, [6,3,4]))
print(bestSum(38, [6,7,12,3,9]))
#print(bestSum(300, [7,14]))
#print(bestSum(100, [1,2,5,25]))