# Problem -- https://www.interviewbit.com/problems/matrix-search/


def binarySearchRow(start, end, A, B, index):
    if start <= end:
        mid = (start + end) // 2
        if A[index][mid] == B:
            return 1
        elif A[index][mid] > B:
            return binarySearchRow(start, mid - 1, A, B, index)
        else:
            return binarySearchRow(mid + 1, end, A, B, index)
    else:
        return 0


def binarySearchColumn(start, end, A, B, N):
    if start <= end:
        mid = (start + end) // 2
        if mid == N - 1 and B > A[mid][0]:
            return mid
        if A[mid][0] <= B and A[mid + 1][0] > B:
            return mid
        elif A[mid][0] > B:
            return binarySearchColumn(start, mid - 1, A, B, N)
        else:
            return binarySearchColumn(mid + 1, end, A, B, N)

    else:
        return -1


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        N = len(A)
        M = len(A[0])
        row_index = 0
        if N != 1:
            row_index = binarySearchColumn(0, N - 1, A, B, N)

        return binarySearchRow(0, M - 1, A, B, row_index)
