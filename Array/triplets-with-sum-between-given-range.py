#Probelm -- https://www.interviewbit.com/problems/triplets-with-sum-between-given-range/


class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        arr = [float(x) for x in A]
        arr.sort()
        n = len(arr)
        i = 0
        j = 1 
        k = n-1
        if n < 3:
            return 0
        if n == 3:
            if sum(arr) > 1 and sum(arr) < 2:
                return 1
            else:
                return 0
                
        while j < k and i < k:
            if arr[i]+arr[j]+arr[k] > 1 and arr[i]+arr[j]+arr[k] < 2:
                return 1
            
            if j+1 == k:
                i += 1
            elif arr[i]+arr[j]+arr[k] < 1:
                j += 1
            else:
                k -= 1
            
            if i != 0 and i == j:
                break
        return 0