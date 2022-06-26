# Problem -- https://www.interviewbit.com/problems/pair-with-given-difference/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        if B < 0:
            B = -B
        i, j, n = 0, 1, len(A)
        while j < n:
            diff = A[j] - A[i]
            if diff == B and i != j:
                return 1
            elif diff > B:
                i += 1
            else:
                j += 1
        return 0
