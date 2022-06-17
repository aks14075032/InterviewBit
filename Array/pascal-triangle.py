# Problem -- https://www.interviewbit.com/problems/pascal-triangle/


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        ans = []
        for line in range(2, A + 2):
            C = 1
            curr = []
            for i in range(1, line + 1):
                if C != 0:
                    curr.append(C)
                C = int(C * (line - i - 1) / i)
            ans.append(curr)
        return ans
