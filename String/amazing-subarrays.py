# Probelm -- https://www.interviewbit.com/problems/amazing-subarrays/

mod = 10003


def isVowel(A):
    if A == "a" or A == "e" or A == "i" or A == "o" or A == "u":
        return 1
    return 0


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        A = A.lower()
        n = len(A)
        ans = 0
        for i in range(len(A)):
            if isVowel(A[i]):
                ans = (ans + (n - i)) % mod
        return ans
