# Problem -- https://www.interviewbit.com/problems/rotated-array/


def pivotBinarySearch(start, end, A):
    if start <= end:
        mid = (start + end) // 2
        if mid < end and A[mid] > A[mid + 1]:
            return A[mid + 1]
        if mid > start and A[mid] < A[mid - 1]:
            return A[mid]
        if A[start] >= A[mid]:
            return pivotBinarySearch(start, mid - 1, A)
        else:
            return pivotBinarySearch(mid + 1, end, A)
    else:
        return -1


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        index = pivotBinarySearch(0, len(A) - 1, A)
        if index == -1:
            return A[0]
        return index
