# Problem -- https://www.interviewbit.com/problems/balance-array/

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        prefix_odd = [0]*n
        prefix_even = [0]*n
        suffix_odd = [0]*n
        suffix_even = [0]*n
        
        prefix_odd[0] = A[0]
        for i in range(1, n):
            if i%2 == 0:
                prefix_odd[i] = prefix_odd[i-1]+A[i]
                prefix_even[i] = prefix_even[i-1]
            else:
                prefix_even[i] = prefix_even[i-1]+A[i]
                prefix_odd[i] = prefix_odd[i-1]
        
        if n%2 != 0: suffix_odd[n-1] = A[n-1]
        else: suffix_even[n-1] = A[n-1]
        
        for i in range(n-2, -1, -1):
            if i%2 == 0:
                suffix_odd[i] = suffix_odd[i+1]+A[i]
                suffix_even[i] = suffix_even[i+1]
            else:
                suffix_even[i] = suffix_even[i+1]+A[i]
                suffix_odd[i] = suffix_odd[i+1]
        
        count = 0
        
        for i in range(0, n):
            if prefix_odd[i] + suffix_even[i] == prefix_even[i]+suffix_odd[i]:
                count += 1
        return count