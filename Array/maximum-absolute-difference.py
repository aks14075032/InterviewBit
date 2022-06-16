#Problem -- https://www.interviewbit.com/problems/maximum-absolute-difference/

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        maxi1 = float('-inf')
        mini1 = float('inf')
        maxi2 = float('-inf')
        mini2 = float('inf')
        
        for i in range(len(A)):
            maxi1 = max(maxi1, A[i]+i)
            maxi2 = max(maxi2, A[i]-i)
            mini1 = min(mini1, A[i]+i)
            mini2 = min(mini2, A[i]-i)
        
        return max(abs(maxi1-mini1), abs(maxi2-mini2))