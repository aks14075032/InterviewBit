# Problem -- https://www.interviewbit.com/problems/count-and-say/


class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        start = "1"
        ans = start
        curr_count = 0
        curr_element = "1"
        for i in range(A - 1):
            if start == "1":
                ans = "11"
                start = ans
                continue
            curr_count = 1
            curr_element = start[0]
            ans = ""
            for j in range(1, len(start)):
                if start[j] == start[j - 1]:
                    curr_count += 1
                else:
                    ans = ans + str(curr_count) + curr_element
                    curr_element = start[j]
                    curr_count = 1

                if j == len(start) - 1:
                    ans = ans + str(curr_count) + curr_element
            start = ans
        return ans
