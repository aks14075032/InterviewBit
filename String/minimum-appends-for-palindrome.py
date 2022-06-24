# problem -- https://www.interviewbit.com/problems/minimum-appends-for-palindrome/


def computeLpsArray(pat, M, lps):
    len = 0
    lps[0] = 0
    i = 1

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        A = A[::-1] + "$" + A
        M = len(A)
        lps = [0] * M
        computeLpsArray(A, M, lps)
        return n - lps[-1]
