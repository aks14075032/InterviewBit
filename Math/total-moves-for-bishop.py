# Python --> https://www.interviewbit.com/problems/total-moves-for-bishop/


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return (
            min(abs(8 - A), abs(8 - B))
            + min(abs(8 - A), abs(1 - B))
            + min(abs(1 - A), abs(8 - B))
            + min(abs(1 - A), abs(1 - B))
        )
