# Problem -- https://www.interviewbit.com/problems/set-matrix-zeros/hints/


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        m = len(A)  # Rows
        n = len(A[0])  # Colums

        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    if A[i][0] != 0:
                        A[i][0] = 2
                    if A[0][j] != 0:
                        A[0][j] = 3

        first_column = False
        first_row = False
        for i in range(m):
            if A[i][0] == 0 or A[i][0] == 2:
                for j in range(1, n):
                    if A[i][j] == 1:
                        A[i][j] = 4
            if A[i][0] == 0:
                first_column = True

        for i in range(n):
            if A[0][i] == 0 or A[0][i] == 3:
                for j in range(1, m):
                    if A[j][i] == 1:
                        A[j][i] = 4
            if A[0][i] == 0:
                first_row = True

        if first_row:
            for i in range(n):
                A[0][i] = 0

        if first_column:
            for i in range(m):
                A[i][0] = 0

        for i in range(m):
            for j in range(n):
                if A[i][j] != 1:
                    A[i][j] = 0
        return A
