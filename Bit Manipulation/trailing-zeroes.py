# Problem -- https://www.interviewbit.com/problems/trailing-zeroes/
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 0
        while A & 1 == 0:
            A = A >> 1
            ans += 1
        return ans
