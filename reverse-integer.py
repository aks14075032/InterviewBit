# Problem -- https://www.interviewbit.com/problems/reverse-integer/


class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        neg = False
        if A < 0:
            neg = True
        A = abs(A)
        rev = 0
        last_digit = False
        while A > 0:
            temp = A % 10
            if temp == 0 and last_digit == False:
                A /= 10
                continue
            rev = int(rev * 10 + temp)
            A = int(A / 10)
            last_digit = True

        if rev >= 2147483647 or rev <= -2147483648:
            return 0
        if neg:
            rev = (-1) * rev
        return rev
