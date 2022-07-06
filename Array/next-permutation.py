# https://www.interviewbit.com/problems/next-permutation/
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        i = len(A) - 2
        while A[i] >= A[i + 1]:
            i = i - 1
            if i < 0:
                break
        if i < 0:
            A = A[::-1]
            return A
        else:
            j = len(A) - 1
            while A[j] <= A[i]:
                j -= 1
            A[i], A[j] = A[j], A[i]
            A[i + 1 :] = sorted(A[i + 1 :])
            return A

        for j in range(n - 1, i, -1):
            if A[j] > x and A[j] < A[smallest]:
                smallest = j

        A[smallest], A[i - 1] = A[i - 1], A[smallest]

        A[i + 1 :].sort()
        return A
