class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        n = len(A)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = A[0]
        suffix[n - 1] = A[n - 1]
        maxi = A[0]
        mini = A[n - 1]
        for i in range(1, n):
            prefix[i] = maxi
            maxi = max(maxi, A[i])
        for i in range(n - 2, -1, -1):
            suffix[i] = mini
            mini = min(mini, A[i])

        for i in range(1, n - 1):
            if A[i] < suffix[i] and A[i] > prefix[i]:
                return 1
        return 0
