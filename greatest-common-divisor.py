# Problem -- https://www.interviewbit.com/problems/greatest-common-divisor/
def gcd_recursive(A, B):
    if A == 0:
        return B
    return gcd_recursive(B % A, A)


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        return gcd_recursive(A, B)
