# Problem -- https://www.interviewbit.com/problems/maximum-sum-triplet/


from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i:
        return i - 1
    else:
        return -1


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        suffix_large = [0] * len(A)
        suffix_large[len(A) - 1] = A[len(A) - 1]
        for i in range(len(A) - 2, -1, -1):
            suffix_large[i] = max(suffix_large[i + 1], A[i])
        ans = 0
        lst = []
        lst.append(A[0])
        for i in range(1, len(A) - 1):
            res = BinarySearch(lst, A[i])
            if res != -1 and A[i] < suffix_large[i + 1]:
                ans = max(ans, lst[res] + A[i] + suffix_large[i + 1])
            lst.insert(res + 1, A[i])
        return ans
