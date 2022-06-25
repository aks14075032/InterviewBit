# Problem -- https://www.interviewbit.com/problems/implement-power-function/
class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x == 0:
            return 0
        res = 1
        while n > 0:
            if n & 1:
                res = (res * x) % d  # N is odd

            n = n >> 1

            x = (x * x) % d

        return (res + d) % d
