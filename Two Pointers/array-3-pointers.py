# Problem -- https://www.interviewbit.com/problems/array-3-pointers/
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        i, j, k = 0, 0, 0
        ans = 9999999999
        while i < len(A) and j < len(B) and k < len(C):
            ans = min(
                ans, max(abs(A[i] - B[j]), max(abs(B[j] - C[k]), abs(C[k] - A[i])))
            )
            if A[i] <= B[j] and A[i] <= C[k]:
                i += 1
            elif B[j] <= A[i] and B[j] <= C[k]:
                j += 1
            else:
                k += 1
        return ans
