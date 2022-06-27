# Problem --https://www.interviewbit.com/problems/number-of-1-bits/
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        ans = 0
        for i in range(32):
            if A & (1 << i):
                ans += 1

        return ans
