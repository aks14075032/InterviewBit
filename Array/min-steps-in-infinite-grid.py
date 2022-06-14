# Problem -- https://www.interviewbit.com/problems/min-steps-in-infinite-grid/


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coverPoints(self, A, B):
        max_steps = 0
        for i in range(1, len(A)):
            max_steps = max_steps + abs(max(abs(A[i] - A[i - 1]), abs(B[i] - B[i - 1])))
        return abs(max_steps)
