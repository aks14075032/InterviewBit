# Problem -- https://www.interviewbit.com/problems/palindromic-binary-representation/


def convertToInt(binary):
    ans = 0
    for i in range(len(binary)):
        ans = ans * 2 + (ord(binary[i]) - ord("0"))
    return ans


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1:
            return 1
        A = A - 1
        q = []
        q.append("11")
        while len(q) != 0:
            curr = q.pop(0)
            A -= 1

            if A == 0:
                return convertToInt(curr)

            lenn = len(curr)
            if lenn % 2 == 0:
                q.append(curr[0 : int(lenn / 2)] + "0" + curr[int(lenn / 2) :])
                q.append(curr[0 : int(lenn / 2)] + "1" + curr[int(lenn / 2) :])
            else:
                midchar = curr[int(lenn / 2)]
                q.append(curr[0 : int(lenn / 2)] + midchar + curr[int(lenn / 2) :])
        return 0
