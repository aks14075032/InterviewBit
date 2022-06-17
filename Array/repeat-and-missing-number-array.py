# Problem -- https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# Solution -- O(n) as numbers are between 1 to n just use the current space and negate the values at current place


class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        ans1 = 0
        ans2 = 0
        arr = list(A)
        n = len(A)
        for i in range(len(arr)):
            if arr[abs(arr[i]) - 1] < 0:
                ans1 = abs(arr[i])

            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

        for i in range(len(arr)):
            if arr[i] > 0 and i + 1 != ans1:
                ans2 = i + 1
                break
        return ans1, ans2
