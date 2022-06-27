# Problem -- https://www.interviewbit.com/problems/intersection-of-sorted-arrays/
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        i, j = 0, 0
        m, n = len(A), len(B)
        ans = []
        while i < m and j < n:
            if A[i] == B[j]:
                ans.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
        return ans
