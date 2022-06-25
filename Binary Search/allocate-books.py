# Problem -- https://www.interviewbit.com/problems/allocate-books/


def isCurrentPossible(A, mid, B):
    countStudents = 1
    curr_sum = 0

    for i in range(len(A)):
        if A[i] > mid:
            return False

        if curr_sum + A[i] > mid:
            countStudents += 1
            curr_sum = A[i]

            if countStudents > B:
                return False
        else:
            curr_sum += A[i]
    return True


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        sumA = sum(A)
        start, end = 0, sumA
        n = len(A)
        if n < B:
            return -1

        result = 10 ** 9
        while start <= end:
            mid = (start + end) // 2
            # print(mid)
            if isCurrentPossible(A, mid, B):
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        return result
