class Solution:
    # @param A : integer
    # @return a list of integers
    def solprimesumve(self, A):
        n = A + 1
        prime = [True] * (n + 1)

        p = 2
        while p * p <= n:
            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        for i in range(2, A):
            if prime[i] and prime[A - i]:
                return [i, A - i]
