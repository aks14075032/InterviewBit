# Problem -- https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        k = 0
        flag = True
        for i in range(1, len(A)):
            if A[k] != A[i]:
                A[k + 1] = A[i]
                k += 1
                flag = True
            elif flag:
                A[k + 1] = A[i]
                k += 1
                flag = False
        return k + 1
