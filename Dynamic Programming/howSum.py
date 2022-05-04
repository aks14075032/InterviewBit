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