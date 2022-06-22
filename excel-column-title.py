# Problem -- https://www.interviewbit.com/problems/excel-column-title/

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
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        ans = ""
        while A > 0:
            if A % 26 == 0:
                ans = "Z" + ans
                A = int(A / 26) - 1
            else:
                index = A % 26
                ans = alpha_list[int(index - 1)] + ans
                A = int(A / 26)
        return ans
