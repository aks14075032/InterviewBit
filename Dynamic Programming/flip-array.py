# https://www.interviewbit.com/problems/flip-array/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        s, n = sum(A) // 2 + 1, len(A) + 1

        dp = [[i and float("inf") or 0] * (n) for i in range(s)]

        for i in range(s):
            for j in range(1, n):
                if i - A[j - 1] >= 0:
                    dp[i][j] = min(dp[i][j - 1], dp[i - A[j - 1]][j - 1] + 1)
                else:
                    dp[i][j] = dp[i][j - 1]

        for row in dp[::-1]:
            if row[-1] < float("inf"):
                return row[-1]
        return None
