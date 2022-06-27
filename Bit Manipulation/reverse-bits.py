# Problem -- https://www.interviewbit.com/problems/reverse-bits/
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        ans = 0
        for i in range(32):
            if A & (1 << i):
                ans += 1 << (31 - i)
        return ans
