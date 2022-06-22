# Problem -- https://www.interviewbit.com/problems/trailing-zeros-in-factorial


class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A, B):
        ans = 0
        while A > 0:
            A //= 5
            ans += A
        return ans
