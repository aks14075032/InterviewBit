# Problem -- https://www.interviewbit.com/problems/smaller-or-equal-elements/


def binarySearchModified(start, end, arr, key):
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] <= key:
            if mid == len(arr) - 1:
                return mid
            elif arr[mid + 1] > key:
                return mid
            else:
                return binarySearchModified(mid + 1, end, arr, key)
        else:
            return binarySearchModified(start, mid - 1, arr, key)
    else:
        return -1


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        index = binarySearchModified(0, len(A) - 1, A, B)
        if index == -1:
            return 0
        return index + 1
