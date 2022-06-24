# Problem -- interviewbit.com/problems/zigzag-string/


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        arr = [""] * B
        forward = True
        j = 0
        if B == 1:
            return A
        for i in range(len(A)):
            arr[j] += A[i]
            if forward:
                j += 1
                if j == B - 1:
                    forward = False
            else:
                j -= 1
                if j == 0:
                    forward = True

        return "".join(arr)
