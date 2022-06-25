# Problem -- https://www.interviewbit.com/problems/woodcutting-made-easy/


def total_wood_cut(value, arr):
    ans = 0
    for i in range(len(arr)):
        if arr[i] - value > 0:
            ans += arr[i] - value
    return ans


def findPerfectIndex(start, end, arr, B):
    if start <= end:
        mid = (start + end) // 2
        total_wood_cut_curr = total_wood_cut(mid, arr)
        total_wood_cut_next = total_wood_cut(mid + 1, arr)
        # print(mid, total_wood_cut_curr, total_wood_cut_next)
        if total_wood_cut_curr >= B and total_wood_cut_next < B:
            return mid
        elif total_wood_cut_curr > B:
            return findPerfectIndex(mid + 1, end, arr, B)
        else:
            return findPerfectIndex(start, mid - 1, arr, B)
    else:
        return -1


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        maxi = max(A)
        return findPerfectIndex(0, maxi, A, B)
