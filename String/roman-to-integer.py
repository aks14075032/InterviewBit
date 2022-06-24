val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        answer = 0
        i = 0
        while i < len(A):
            if i + 1 < len(A):
                try:
                    index = rom.index(A[i] + A[i + 1])
                    i += 2
                except:
                    index = rom.index(A[i])
                    i += 1
                answer += val[index]
            else:
                index = rom.index(A[i])
                answer += val[index]
                i += 1

        return answer
