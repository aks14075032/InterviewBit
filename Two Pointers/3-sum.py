# Problem -- https://www.interviewbit.com/problems/3-sum/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        best_sum = A[0] + A[1] + A[2]
        minDiff = B - best_sum
        n = len(A)
        for k in range(0, n - 2):
            i, j = k + 1, n - 1
            while i < j:
                temp = A[i] + A[j] + A[k]
                diff = abs(temp - B)
                if diff == 0:
                    return B
                elif temp > B:
                    j -= 1
                else:
                    i += 1
                if minDiff > diff:
                    minDiff = diff
                    best_sum = temp
        return best_sum
