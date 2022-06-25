# Problem -- https://www.interviewbit.com/problems/painters-partition-problem/

mod = 10000003


def isPaintPossible(arr, mid, A):
    painterCount = 1
    curr_sum = 0
    for i in range(len(arr)):
        if arr[i] > mid:
            return False

        if arr[i] + curr_sum > mid:
            painterCount += 1
            curr_sum = arr[i]

            if painterCount > A:
                return False
        else:
            curr_sum += arr[i]
    return True


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def searchRange(self, A, B, C):
        sumPaintingBoards = sum(C)

        start, end = 0, sumPaintingBoards

        result = 10000002

        while start <= end:
            mid = (start + end) // 2

            if isPaintPossible(C, mid, A):
                result = ((mid % mod) * (B % mod)) % mod
                end = mid - 1
            else:
                start = mid + 1
        return result
