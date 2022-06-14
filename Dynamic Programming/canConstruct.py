from operator import truediv


def canConstruct(target, wordBank, memo=None):
    if target == "":
        return True
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target.removeprefix(word)
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                return True

    memo[target] = False
    return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(
    canConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee"],
    )
)
