# Problem -- https://www.interviewbit.com/problems/flip/
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        ans = []
        n = len(A)
        sumA, max_sum = 0, -1
        isZero, isOne = 0, 0
        a, b, x = 1, 1, 1
        for i in range(n):
            if A[i] == "0":
                sumA += 1
                isZero = 1
            else:
                sumA -= 1
                isOne = 1
            if sumA < 0:
                sumA = 0
                x = i + 2
                continue
            if sumA > max_sum:
                max_sum = sumA
                a = x
                b = i + 1
        if isZero == 0:
            return ans
        if isOne == 0:
            a = 1
            b = n
        ans.append(a)
        ans.append(b)
        return ans
