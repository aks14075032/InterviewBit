# Problem -- https://www.interviewbit.com/problems/single-number-ii/
class Solution:
    # @param A: tuple of integers
    # @return an integer
    def singleNumber(self, A):
        temp = [0] * 32

        for i in range(32):
            for j in range(len(A)):
                if A[j] & (1 << i):
                    temp[i] += 1

        ans = 0
        for i in range(32):
            if temp[i] % 3 != 0:
                ans += 1 << i
        return ans
