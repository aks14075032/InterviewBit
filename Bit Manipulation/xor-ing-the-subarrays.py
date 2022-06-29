# Problem -- https://www.interviewbit.com/problems/xor-ing-the-subarrays/
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) % 2 == 0:
            return 0
        ans = 0
        for i in range(len(A)):
            if i % 2 == 0:
                ans = ans ^ A[i]
        return ans
