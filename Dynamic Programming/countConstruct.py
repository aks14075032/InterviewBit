from operator import truediv


def countConstruct(target, wordBank, memo=None):
    if target == '': return 1
    if memo is None:
        memo = {}
    if target in memo: return memo[target]
    totalCount = 0
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target.removeprefix(word)
            currentNumberWays = countConstruct(suffix, wordBank, memo)
            totalCount += currentNumberWays  
    memo[target]=totalCount
    return totalCount

print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
    [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee'
    ]
))