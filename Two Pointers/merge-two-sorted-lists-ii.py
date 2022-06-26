# Problem -- https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/hints/
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        i, j = 0, 0
        m, n = len(A), len(B)
        while j < n:
            if i >= len(A):
                A.insert(i, B[j])
                j += 1
            elif A[i] > B[j]:
                A.insert(i, B[j])
                j += 1
            i += 1
        while j < n:
            A.append(B[j])
            j += 1
        return A
