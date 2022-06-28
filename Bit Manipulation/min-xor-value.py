# PROBLEM -- https://www.interviewbit.com/problems/min-xor-value/
class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        ans = 999999999
        for i in range(1, len(A)):
            ans = min(ans, A[i] ^ A[i - 1])
        return ans
