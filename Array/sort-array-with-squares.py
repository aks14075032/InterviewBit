import bisect
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        for i in range(len(A)):
            bisect.insort(ans, A[i]*A[i])
        return ans