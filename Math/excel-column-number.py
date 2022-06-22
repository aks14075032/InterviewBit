# Problem -- https://www.interviewbit.com/problems/excel-column-number/

alpha_list = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        n = len(A)
        j = 0
        ans = 0
        for i in range(n - 1, -1, -1):
            index = alpha_list.index(A[i])
            index = index + 1
            ans += index * pow(26, j)
            j += 1
        return ans
