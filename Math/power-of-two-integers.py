# Problem -- https://www.interviewbit.com/problems/power-of-two-integers/

import math


class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A <= 1:
            return 1

        for i in range(2, int(math.sqrt(A)) + 1):
            p = math.log(A) / math.log(i)

            if round((p - int(p)), 8) < 0.00000001:
                return 1
        return 0
