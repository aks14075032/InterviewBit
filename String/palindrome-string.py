# Problem --    https://www.interviewbit.com/problems/palindrome-string/


class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        new_string = "".join(e for e in A if e.isalnum())
        new_string = new_string.upper()
        rev_string = new_string[::-1]
        if new_string == rev_string:
            return 1
        return 0
