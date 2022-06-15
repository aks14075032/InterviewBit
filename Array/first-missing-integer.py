#Problem -- https://www.interviewbit.com/problems/first-missing-integer/hints/

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        maxi = max(A)
        if maxi <= 0:
            return 1
        
        for ele in A:
            if ele <= 0:
                A.remove(ele)           
                
        if A[-1] <= 0: A.remove(A[-1])
        n = len(A)
        
        for i in range(n):
            if abs(A[i]) < n:
                if A[abs(A[i])] > 0:
                    A[abs(A[i])] = -A[abs(A[i])]
        
        for i in range(1, n):
            if A[i] > 0:
                return i
        return n+1
        