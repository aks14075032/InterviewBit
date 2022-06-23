# Problem -- https://www.interviewbit.com/problems/remove-consecutive-characters/


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        ans = ""
        curr_string = A[0]
        if B == 1:
            return ans

        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                curr_string += A[i]
            else:
                ans += curr_string
                curr_string = A[i]

            if len(curr_string) == B:
                curr_string = ""
        if curr_string:
            ans += curr_string
        return ans
