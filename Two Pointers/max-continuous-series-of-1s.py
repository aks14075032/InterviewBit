# Problem -- https://www.interviewbit.com/problems/max-continuous-series-of-1s/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        zeroUsed = 0
        max_count = 0
        start = 0
        end = 0
        i, j, n = 0, 0, len(A)
        while i < n:
            if A[i] == 0:
                zeroUsed += 1
            while zeroUsed > B:
                if A[j] == 0:
                    zeroUsed -= 1
                j += 1
            # print(i, j)
            curr = i - j + 1
            if curr > max_count:
                max_count = curr
                start = j
                end = i
            i += 1
        ans = [i for i in range(start, end + 1)]
        return ans
