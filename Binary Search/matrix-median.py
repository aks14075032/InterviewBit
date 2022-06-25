# Problem -- https://www.interviewbit.com/problems/matrix-median/

from bisect import bisect_right as upper_bound


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        M, N = len(A), len(A[0])
        mini = A[0][0]
        maxi = A[0][N - 1]

        for i in range(M):
            mini = min(mini, A[i][0])
            maxi = max(maxi, A[i][N - 1])

        required = ((M * N) + 1) // 2
        # print(mini, maxi)
        while mini < maxi:
            mid = (mini + maxi) // 2
            count = [0]
            for i in range(M):
                j = upper_bound(A[i], mid)
                count[0] += j
            if count[0] < required:
                mini = mid + 1
            else:
                maxi = mid

        return mini
