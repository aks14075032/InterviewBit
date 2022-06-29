# Problem -- https://www.interviewbit.com/problems/different-bits-sum-pairwise/
mod = 1000000007


class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        temp = [0] * 32
        for i in range(32):
            for j in range(len(A)):
                if A[j] & (1 << i):
                    temp[i] += 1
        ans = 0
        for i in range(32):
            ans = (ans + (temp[i] * ((2 * (len(A) - temp[i])) % mod)) % mod) % mod
        return ans
