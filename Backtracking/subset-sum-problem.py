def isSubsetSum(arr, n, target_sum, ans):
    if target_sum == 0:
        return True

    if n == 0:
        return False

    if arr[n - 1] > target_sum:
        isSubsetSum(arr, n - 1, target_sum, ans)

    return isSubsetSum(arr, n - 1, target_sum, ans) or isSubsetSum(
        arr, n - 1, target_sum - arr[n - 1], ans
    )


def isSubsetSumDP(arr, n, target_sum):
    dp = [[False for i in range(target_sum + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, target_sum + 1):
        dp[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    ans = []

    return dp[n][target_sum]


set = [3, 34, 4, 12, 5, 2]
sum = 9
ans = []
n = len(set)
if isSubsetSum(set, n, sum, ans) == True:
    print("Found a subset with given sum")
else:
    print("No subset with given sum")

if isSubsetSumDP(set, n, sum) == True:
    print("Found a subset with given sum")
else:
    print("No subset with given sum")
