val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        ans = ""
        for i in range(13):
            while A >= val[i]:
                ans += rom[i]
                A -= val[i]
        return ans
