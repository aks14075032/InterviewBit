# Problem -- https://www.interviewbit.com/problems/convert-to-palindrome/


def isPalindrome(str1):
    if str1 == str1[::-1]:
        return 1
    return 0


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        i, j = 0, len(A) - 1
        flag = False
        while i < j:
            if A[i] == A[j]:
                i += 1
                j -= 1
            else:
                if isPalindrome(A[:i] + A[i + 1 :]) or isPalindrome(A[:j] + A[j + 1 :]):
                    return 1
                else:
                    return 0
        return 1
