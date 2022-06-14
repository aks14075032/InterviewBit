#Problem -- https://www.interviewbit.com/problems/minimum-lights-to-activate/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        temp_index = B-1
        ans = 0
        prev_index = 0
        check = 0
        while temp_index < len(A):
            if temp_index <= prev_index:
                return -1
            if A[temp_index] == 1:
                prev_index = temp_index
                temp_index = temp_index+2*B
                ans = ans +1
                if prev_index + B >= len(A) - 1:
                    return ans
                if check == 0 and temp_index >= len(A):
                    temp_index = len(A)-1
            else:
                temp_index = temp_index - 1
        if ans == 0: ans = 1
        return ans
