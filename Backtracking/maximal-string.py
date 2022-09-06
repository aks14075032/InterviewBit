# Problem -- https://www.interviewbit.com/problems/maximal-string/
def swap(string, i, j):

    return string[:i] + string[j] + string[i + 1 : j] + string[i] + string[j + 1 :]


def findMaximumNum(string, k, maxm):

    if k == 0:
        return

    n = len(string)

    for i in range(n - 1):

        for j in range(i + 1, n):

            if string[i] < string[j]:
                string = swap(string, i, j)

                if string > maxm[0]:
                    maxm[0] = string

                findMaximumNum(string, k - 1, maxm)

                string = swap(string, i, j)


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        n = len(A)
        maxm = [A]
        findMaximumNum(A, B, maxm)
        return maxm[0]
