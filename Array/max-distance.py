# https://www.interviewbit.com/problems/max-distance/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        new_A = [(A[i], i) for i in range(len(A))]
        new_A.sort()
        ans = 0
        n = len(new_A)
        rmax = new_A[n - 1][1]
        for i in range(len(new_A) - 2, -1, -1):
            ans = max(ans, rmax - new_A[i][1])
            rmax = max(rmax, new_A[i][1])
        return ans
