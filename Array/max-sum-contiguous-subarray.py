# Problem -- https://www.interviewbit.com/problems/max-sum-contiguous-subarray/


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        arr = list(A)
        maxi = max(arr)
        if maxi <= 0:
            return maxi

        maxi_sum = 0
        curr_sum = 0

        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum <= 0:
                curr_sum = 0

            if curr_sum > maxi_sum:
                maxi_sum = curr_sum

        return maxi_sum
