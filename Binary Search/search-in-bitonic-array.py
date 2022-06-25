# Problem -- https://www.interviewbit.com/problems/search-in-bitonic-array/


def ascendingBinarySearch(start, end, element, arr):
    # print("asce--> ", start, end)
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            return ascendingBinarySearch(start, mid - 1, element, arr)
        else:
            return ascendingBinarySearch(mid + 1, end, element, arr)
    else:
        return -1


def descendingBinarySearch(start, end, element, arr):
    # print("decen--> ", start, end)
    if start <= end:
        mid = (start + end) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            return descendingBinarySearch(start, mid - 1, element, arr)
        else:
            return descendingBinarySearch(mid + 1, end, element, arr)
    else:
        return -1


def findBitonicPoint(start, end, arr):
    bitonicPoint = 0
    mid = (start + end) // 2

    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
        return mid
    elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
        bitonicPoint = findBitonicPoint(mid, end, arr)
    else:
        bitonicPoint = findBitonicPoint(start, mid, arr)
    return bitonicPoint


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        index = findBitonicPoint(0, len(A) - 1, A)

        ans = ascendingBinarySearch(0, index, B, A)
        if ans != -1:
            return ans

        ans = descendingBinarySearch(index, len(A) - 1, B, A)
        return ans
