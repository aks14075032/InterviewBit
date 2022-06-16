#Problem -- interviewbit.com/problems/add-one-to-number/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)
        if A == [9] * n:
            return [1] + [0] * n

        for i in range(n - 1, -1, -1):
            A[i] = (A[i] + 1) % 10
            if A[i] != 0:
                break
        
        startIdx = 0
        while startIdx < n:
            if A[startIdx] != 0:
                break
            startIdx += 1

        return A[startIdx:]