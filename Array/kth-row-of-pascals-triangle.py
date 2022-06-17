# Problem -- https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/
# Solution Approcation -- Each element represents C(line, i)   = line! / ( (line-i)! * i! )
# Solve the above equation to get C(line, i) = C(line, i-1) * (line - i + 1) / i


class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        A = A + 1
        pascal_ans = [0] * A
        C = 1
        for i in range(1, A + 1):
            pascal_ans[i - 1] = C
            C = int(C * (A - i) / i)
        return pascal_ans
