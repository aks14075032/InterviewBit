# Problem -- https://www.interviewbit.com/problems/maximum-ones-after-modification/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        zeroUsed = 0
        j = 0
        n = len(A)
        ans = 0
        for i in range(n):
            if A[i] == 0:
                zeroUsed += 1

            while zeroUsed > B:
                if A[j] == 0:
                    zeroUsed -= 1
                j += 1
            ans = max(ans, i - j + 1)

        return ans
