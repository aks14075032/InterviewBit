# Problem -- https://www.interviewbit.com/problems/step-by-step/

import math


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 0
        A = abs(A)
        n = math.ceil(
            (math.sqrt(1 + 8 * A) - 1) / 2
        )  # n^2+n-2*A #Refer here https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/

        sm = (n * (n + 1)) / 2
        n = int(n)

        if sm == A:
            return n

        d = sm - A

        if (d % 2) == 0:
            return n
        else:
            if (n % 2) == 1:
                return n + 2
            else:
                return n + 1
