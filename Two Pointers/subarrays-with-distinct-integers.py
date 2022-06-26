# Problem -- https://www.interviewbit.com/problems/subarrays-with-distinct-integers/
def possibleCount(A, B):
    map = {}
    ans = 0
    left, right = 0, 0
    n = len(A)
    while right < n:
        if A[right] not in map:
            map[A[right]] = 0
        map[A[right]] += 1
        while len(map) > B:
            if A[left] not in map:
                map[A[left]] = 0
            map[A[left]] -= 1
            if map[A[left]] == 0:
                del map[A[left]]
            left += 1
        ans += right - left + 1
        right += 1

    return ans


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans1 = possibleCount(A, B)
        ans2 = possibleCount(A, B - 1)
        # print(ans1, ans2)
        return ans1 - ans2
