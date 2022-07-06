# https://www.interviewbit.com/problems/rotate-matrix/
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        N = len(A)

        for x in range(0, int((N + 1) / 2)):
            for y in range(x, N - x - 1):
                temp = A[x][y]
                A[x][y] = A[N - y - 1][x]
                A[N - y - 1][x] = A[N - x - 1][N - y - 1]
                A[N - x - 1][N - y - 1] = A[y][N - x - 1]
                A[y][N - x - 1] = temp
        return A
