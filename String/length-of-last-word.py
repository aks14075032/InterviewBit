# Problem -- https://www.interviewbit.com/problems/length-of-last-word/


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        m = len(A)
        if m == 0:
            return 0
        arr = A.split(" ")
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if len(arr[i]) > 0:
                return len(arr[i])
        return 0
