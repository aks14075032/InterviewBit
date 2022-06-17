# Problem -- https://www.interviewbit.com/problems/largest-number/hints/

from functools import cmp_to_key


@cmp_to_key
def custom_compare(x, y):
    value1 = str(x) + str(y)
    value2 = str(y) + str(x)

    if value1 < value2:
        return 1
    if value2 < value1:
        return -1
    else:
        return 0


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        arr = list(A)
        arr.sort(key=custom_compare)

        result = "".join(map(str, arr))

        if result == "0" * len(arr):
            return "0"

        return result
