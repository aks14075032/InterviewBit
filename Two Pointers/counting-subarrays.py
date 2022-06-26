# Problem -- https://www.interviewbit.com/problems/counting-subarrays/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        sum = 0
        i, j = 0, 0
        while i < (len(A)):
            sum += A[i]
            while sum >= B:
                sum -= A[j]
                j += 1
            ans += i - j + 1
            i += 1
        return ans
