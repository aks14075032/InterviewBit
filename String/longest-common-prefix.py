# Problem -- https://www.interviewbit.com/problems/longest-common-prefix/


def commonPrefix(s1, s2):
    ans = ""
    n = min(len(s1), len(s2))
    for i in range(n):
        if s1[i] == s2[i]:
            ans += s1[i]
    return ans


class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        ans = A[0]
        for i in range(1, len(A)):
            ans = commonPrefix(ans, A[i])
        return ans
