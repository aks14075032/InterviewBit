# https://www.interviewbit.com/problems/maximum-unsorted-subarray/
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        s, e = -1, -1
        n = len(A)
        for i in range(0, n - 1):
            if A[i] > A[i + 1]:
                s = i
                break

        if s == -1:
            return [-1]

        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                e = i
                break

        maxi = A[s]
        mini = A[s]
        # print(s, e)
        for i in range(s + 1, e + 2):
            if A[i] > maxi:
                maxi = A[i]
            if A[i] < mini:
                mini = A[i]

        # print(mini, maxi)
        for i in range(s):
            if A[i] > mini:
                s = i
                break
        # print(e, maxi)
        for i in range(n - 1, e, -1):
            # print(A[i])
            if A[i] < maxi:
                e = i
                # print(e)
                break
        return [s, e]
