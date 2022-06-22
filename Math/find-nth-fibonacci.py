# Problem -- https://www.interviewbit.com/problems/find-nth-fibonacci/hints/
mod = 1000000007


def multiply(f, m):

    a = (f[0][0] * m[0][0] % mod + f[0][1] * m[1][0] % mod) % mod
    b = (f[0][0] * m[0][1] % mod + f[0][1] * m[1][1] % mod) % mod
    c = (f[1][0] * m[0][0] % mod + f[1][1] * m[1][0] % mod) % mod
    d = (f[1][0] * m[0][1] % mod + f[1][1] * m[1][1] % mod) % mod
    f[0][0] = a
    f[0][1] = b
    f[1][0] = c
    f[1][1] = d


def power(F, n):
    if n == 0 or n == 1:
        return
    M = [[1, 1], [1, 0]]

    power(F, n // 2)
    multiply(F, F)

    if n % 2 != 0:
        multiply(F, M)


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        n = A
        F = [[1, 1], [1, 0]]
        if n == 0:
            return 0
        power(F, n - 1)

        return F[0][0]
