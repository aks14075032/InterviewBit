# Problem -- https://www.interviewbit.com/problems/sorted-insert-position/
def binarySearch(start, end, A, B):
    if start <= end:
        mid = (start + end) // 2
        # print(start, end, mid)
        if A[mid] == B:
            return mid
        if mid == 0 and A[mid] > B:
            return mid
        if mid == len(A) - 1 and A[mid] < B:
            return mid + 1
        if A[mid] < B and A[mid + 1] > B:
            return mid + 1
        elif A[mid] < B:
            return binarySearch(mid + 1, end, A, B)
        else:
            return binarySearch(start, mid - 1, A, B)
    else:
        return -1


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        return binarySearch(0, len(A) - 1, A, B)
