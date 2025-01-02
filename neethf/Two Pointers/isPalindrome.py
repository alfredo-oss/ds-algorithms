"""
input: str (a string containing sequential elements)
output: bool (boolean value indicating if the string is or not a palindrome)

notes:
-----
is it ok to assume that the string is cleaned at the moment of entering the input?
* the complexity of this question is to deal with non-alphanum characters.
* in the case that you are asked to create your own alphanum checker the solution would look like this:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            while L < R and not self.alphaNum(s[L]):
                L += 1
            while R > L and not self.alp
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1
        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while R > L and not s[R].isalnum():
                R -= 1    
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True