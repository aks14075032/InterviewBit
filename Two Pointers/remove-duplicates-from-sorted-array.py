# Problem -- https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i, j = 0, 1
        n = len(A)
        ans = 0
        if n == 1:
            return 1
        while j < n:
            if A[i] != A[j]:
                A[i + 1] = A[j]
                i += 1
            j += 1

        return i + 1
