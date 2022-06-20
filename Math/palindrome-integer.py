#Problem -- https://www.interviewbit.com/problems/palindrome-integer/

import math
class Solution:
	# @param A : integer
	# @return an integer
    #No extra space
    def isPalindrome(self, A):
        rev = 0
        num = A 
        while num > 0:
            temp = num % 10
            rev = rev*10 + temp
            num = math.floor(num/10)
        
        if A == rev:
            return 1
        return 0