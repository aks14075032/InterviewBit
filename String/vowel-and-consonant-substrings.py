# Problem -- https://www.interviewbit.com/problems/vowel-and-consonant-substrings/

mod = 1000000007


def isVowel(A):
    if A == "a" or A == "e" or A == "i" or A == "o" or A == "u":
        return 1
    return 0


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowelCount = 0
        constantCount = 0
        ans = 0
        for i in range(len(A)):
            if isVowel(A[i]):
                vowelCount += 1
            else:
                constantCount += 1

        for i in range(len(A)):
            if isVowel(A[i]):
                ans += constantCount % mod
                vowelCount -= 1
            else:
                ans += vowelCount % mod
                constantCount -= 1
        return ans % mod
