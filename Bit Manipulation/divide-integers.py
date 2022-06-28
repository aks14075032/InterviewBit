# Problem -- https://www.interviewbit.com/problems/divide-integers/
INT_MAX = pow(2, 31) - 1


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        sign = -1 if ((A < 0) ^ (B < 0)) else 1

        A = abs(A)
        B = abs(B)

        ans = 0
        temp = 0

        for i in range(31, -1, -1):
            if (temp + (B << i)) <= A:
                temp += B << i
                ans |= 1 << i

        if ans > INT_MAX:
            ans = INT_MAX
            if sign == -1:
                ans = INT_MAX + 1
        return sign * ans
