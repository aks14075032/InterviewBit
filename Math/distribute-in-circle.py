# Problem -- https://www.interviewbit.com/problems/distribute-in-circle/


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return (A - 1 + C) % B
