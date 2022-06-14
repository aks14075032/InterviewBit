def allConstruct(target, wordBank, memo=None):
    if target == "":
        return [[]]
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    result = []
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target.removeprefix(word)
            currentWays = allConstruct(suffix, wordBank, memo)
            targetWays = currentWays
            if targetWays is not None:
                temp = [x.append(word) for x in targetWays]
                result.extend(targetWays)

    # memo[target] = result
    return result


print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
