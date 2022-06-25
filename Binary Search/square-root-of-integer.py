# Problem -- https://www.interviewbit.com/problems/square-root-of-integer/
def binarySearch(start, end, A):
    if start <= end:
        mid = (start + end) // 2
        if (mid * mid) <= A and ((mid + 1) * (mid + 1)) > A:
            return mid
        elif (mid * mid) > A:
            return binarySearch(start, mid - 1, A)
        else:
            return binarySearch(mid + 1, end, A)
    else:
        return -1


class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        return binarySearch(0, A, A)
