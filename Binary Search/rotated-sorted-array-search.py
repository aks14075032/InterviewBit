#Problem -- https://www.interviewbit.com/problems/rotated-sorted-array-search/
def binarySearch(start, end, arr, key):
    if start <= end:
        mid = (start+end) //2
        #print(mid)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binarySearch(start, mid-1, arr, key)
        else:
            return binarySearch(mid+1, end, arr, key)
    else:
        return -1
def pivotBinarySearch(start, end, arr):
    if start <= end:
        mid = (start+end) //2
        if mid < end and arr[mid] > arr[mid+1]:
            return mid
        if mid > start and arr[mid] < arr[mid-1]:
            return mid-1
        if arr[start] >= arr[mid]:
            return pivotBinarySearch(start, mid-1, arr)
        else:
            return pivotBinarySearch(mid+1, end, arr)
    else:
        return -1
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        arr = list(A)
        index = pivotBinarySearch(0, len(arr)-1, arr)
        if index == -1:
            index = 0
        #print(index)
        temp = binarySearch(0, index, arr, B)
        if temp != -1:
            return temp
        temp = binarySearch(index+1, len(arr)-1, arr, B)
        return temp