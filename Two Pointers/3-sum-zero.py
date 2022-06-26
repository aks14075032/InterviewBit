# Problem -- https://www.interviewbit.com/problems/3-sum-zero/
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        n = len(A)
        ans = []
        for j in range(0, n - 2):
            i, k = j + 1, n - 1
            while i < k:
                # print(i, j, k)
                temp = A[i] + A[j] + A[k]
                if temp == 0:
                    curr = [A[j], A[i], A[k]]
                    if curr not in ans:
                        ans.append(curr)
                    i += 1
                elif temp > 0:
                    k -= 1
                else:
                    i += 1
        return ans
