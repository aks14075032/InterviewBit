#Problem -- https://www.interviewbit.com/problems/next-similar-number/

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        mini = [0]*10
        mini[int(A[len(A)-1])] = len(A)-1
        for i in range(len(A)-2, -1, -1):
            if A[i] < A[i+1]:
                temp = A[i]
                list1 = list(A)
                for j in range(int(A[i])+1,10):
                    if mini[j] > 0:
                        list1[i] = j
                        list1[mini[j]] = temp
                        break
            
                A = ''.join(str(v) for v in list1)
                res = ''.join(sorted(A[i+1:]))
                return A[:i+1]+res
            else:
                mini[int(A[i])] = i
        return -1