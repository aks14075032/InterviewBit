# Problem -- https://www.interviewbit.com/problems/count-total-set-bits/

mod = 1000000007


def nearest2Power(A):
    ans = 0
    while (1 << ans) <= A:
        ans += 1
    return (ans - 1) % mod


def solution(A):
    if A == 0:
        return 0
    n = nearest2Power(A)
    countTill2PowerA = (n * (pow(2, n - 1)) % mod) % mod
    msbTillA = A - (((1 << n)) % mod) + 1
    rest = A - ((1 << n) % mod)
    ans = countTill2PowerA + msbTillA + solution(rest)
    return int(ans % mod)


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0 or A == 1:
            return A
        return solution(A)
