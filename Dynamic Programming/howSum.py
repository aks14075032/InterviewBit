#Write a function howSum(targetSum, numbers) that takes in a target sum and an array of numbers as arguments.
#The function should return an array containing any combination of elements that add up to exactly the target sum. If there is no combination that adds up to the target sum, then return null.
#If there are multiple combinations possible, you may return any single one.

#Solution --> Solved with help of dynamic programming.


def howSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    
    if targetSum in memo: return memo[targetSum]
    if targetSum < 0: return None
    if targetSum == 0: return []

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult is not None:
            remainderResult.append(num)
            memo[targetSum] = remainderResult
            return memo[targetSum]
    
    memo[targetSum]=None
    return None

print(howSum(10, [6,3,4]))
print(howSum(38, [6,7,12,3,9]))
print(howSum(300, [7,14]))