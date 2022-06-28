# Problem -- https://www.interviewbit.com/problems/single-number/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = A[0]
        for i in range(1, len(A)):
            ans ^= A[i]
        return ans
