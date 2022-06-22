# Problem -- https://www.interviewbit.com/problems/sum-of-pairwise-hamming-distance/

modulo = 1000000007


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistanceoes(self, A):
        ans = 0
        n = len(A)
        for i in range(0, 32):
            count = 0
            for j in range(n):
                if A[j] & (1 << i):
                    count += 1
            ans = (
                ans % modulo
                + ((((count % modulo) * (n - count) % modulo) % modulo) * 2) % modulo
            ) % modulo

        return ans
