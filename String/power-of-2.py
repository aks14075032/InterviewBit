# Problem -- https://www.interviewbit.com/problems/power-of-2/


class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        x = int(A)
        if x == 1:
            return 0
        return int(x and (not (x & (x - 1))))
