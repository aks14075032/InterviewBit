# Problem -- https://www.interviewbit.com/problems/search-for-a-range/


def binarySearchStart(start, end, A, B):
    if start <= end:
        mid = (start + end) // 2
        if mid == 0 and A[mid] == B:
            return mid
        if A[mid] == B and A[mid - 1] != B:
            return mid
        elif A[mid] >= B:
            return binarySearchStart(start, mid - 1, A, B)
        else:
            return binarySearchStart(mid + 1, end, A, B)
    else:
        return -1


def binarySearchEnd(start, end, A, B):
    if start <= end:
        mid = (start + end) // 2
        if mid == len(A) - 1 and A[mid] == B:
            return mid
        if A[mid] == B and A[mid + 1] != B:
            return mid
        elif A[mid] > B:
            return binarySearchEnd(start, mid - 1, A, B)
        else:
            return binarySearchEnd(mid + 1, end, A, B)
    else:
        return -1


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        arr = list(A)
        ans = []
        temp1 = binarySearchStart(0, len(arr) - 1, arr, B)
        temp2 = binarySearchEnd(0, len(arr) - 1, arr, B)
        ans.append(temp1)
        ans.append(temp2)
        return ans
