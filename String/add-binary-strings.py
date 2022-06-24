# Problem -- https://www.interviewbit.com/problems/add-binary-strings/


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        carry = 0
        ans = ""
        if len(A) < len(B):
            n = len(B) - len(A)
            A = A.rjust(n + len(A), "0")
        if len(A) > len(B):
            n = len(A) - len(B)
            B = B.rjust(n + len(B), "0")

        i, j = len(A) - 1, len(B) - 1
        while i > -1 or j > -1:
            sum = int(A[i]) + int(B[j]) + carry
            ans = str(sum % 2) + ans
            if sum > 1:
                carry = 1
            else:
                carry = 0
            i -= 1
            j -= 1

        if carry > 0:
            ans = "1" + ans
        return ans
