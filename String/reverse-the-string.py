# Problem -- https://www.interviewbit.com/problems/reverse-the-string/


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        arr = A.split(" ")
        ans = ""
        for i in range(len(arr) - 1, -1, -1):
            if len(arr[i]) != 0:
                ans += arr[i]
                if i != 0:
                    ans += " "
        return ans.rstrip()
