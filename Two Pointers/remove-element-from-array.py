# Problem -- https://www.interviewbit.com/problems/remove-element-from-array/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        k = 0
        for i in range(len(A)):
            if A[i] != B:
                A[k] = A[i]
                k = k + 1
        return k
