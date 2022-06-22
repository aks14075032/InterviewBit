# Problem -- https://www.interviewbit.com/problems/is-rectangle/
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        if (A == B and C == D) or (A == C and B == D) or (A == D and C == B):
            return 1
        return 0
