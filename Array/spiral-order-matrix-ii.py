class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        m, n = A, A
        arr = [[0 for j in range(n)] for i in range(m)]

        k, l = 0, 0
        val = 1
        while k < m and l < n:
            # Top row filling
            for i in range(l, n):
                arr[k][i] = val
                val += 1
            k += 1

            # Last column filling
            for i in range(k, m):
                arr[i][n - 1] = val
                val += 1
            n -= 1

            # Bottom row filling
            if k < m:
                for i in range(n - 1, l - 1, -1):
                    arr[m - 1][i] = val
                    val += 1

            m -= 1

            # First Column
            if l < n:
                for i in range(m - 1, k - 1, -1):
                    arr[i][l] = val
                    val += 1

            l += 1

        return arr
