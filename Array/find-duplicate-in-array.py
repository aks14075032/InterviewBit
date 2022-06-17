class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        arr = list(A)
        n = len(arr)
        for i in range(n):
            if arr[abs(arr[i])] < 0:
                return abs(A[i])
            arr[abs(arr[i])] = -arr[abs(arr[i])]
