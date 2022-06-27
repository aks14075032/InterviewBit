# Problem -- https://www.interviewbit.com/problems/sort-by-color/
class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        n = len(A)
        i, j, k = 0, 1, n - 1
        while j <= k:
            if i == j:
                j += 1
            elif A[j] == 0:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
                i += 1
            elif A[j] == 2:
                temp = A[k]
                A[k] = A[j]
                A[j] = temp
                # print(k, A[k])
                k -= 1
            else:
                j += 1
        return A
