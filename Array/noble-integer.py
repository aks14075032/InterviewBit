#Problem -- https://www.interviewbit.com/problems/noble-integer/

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A.sort()
        for i in range(n-1):
            if A[i] == n-i-1 and A[i] != A[i+1]:
                return 1
        
        if A[n-1] == 0: return 1
        return -1