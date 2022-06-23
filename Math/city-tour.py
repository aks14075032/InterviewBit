# Problem -- https://www.interviewbit.com/problems/city-tour/
M = 1000000007


def power(x, y):

    result = 1
    while y > 0:
        if y % 2 == 0:
            # y is even

            x = (x * x) % M
            y = y / 2

        else:
            # y isn't even

            result = (result * x) % M
            y = y - 1

    return result % M


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        B.sort()
        k = len(B)
        un_vis = []
        un_vis.append(B[0] - 1)
        for i in range(1, k):
            un_vis.append(B[i] - B[i - 1] - 1)
        un_vis.append(A - B[k - 1])

        n = len(un_vis)
        fact = [1] * 100000

        for i in range(1, 100000):
            fact[i] = (fact[i - 1] * i) % M

        ans, x, p = 1, A - k, 1
        for i in range(n):
            if un_vis[i] != 0:
                if i != 0 and i != n - 1:
                    ans = (((ans) % M) * (power(2, un_vis[i] - 1)) % M) % M
                p = (p * fact[un_vis[i]]) % M

        ans = (ans * fact[x]) % M
        ans = (ans * (power(p, M - 2) % M)) % M
        return ans
