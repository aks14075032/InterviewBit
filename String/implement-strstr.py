def computeLpsArray(pat, M, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = 1
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0] * M
    computeLpsArray(pat, M, lps)

    i, j = 0, 0
    while i < N:
        if txt[i] == pat[j]:
            i += 1
            j += 1

        if j == M:
            return i - j

        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        return KMPSearch(B, A)
