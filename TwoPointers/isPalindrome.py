"""
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backwards.
The palindrome ignores all alphanumeric characters.
Assuming that I could only read the alphanumeric characters....(Can worry about this later)
-> For example: "wasitacaroracatisaw"
I could start at the top and end of the array, asking: Are these two characters equal?
Then I would repeat that question for the two elements at hand, until the entire array is traversed and if the two elements im looking at are the same.
Otherwise I should return "false".
Remember that this is assuming you already cleaned the string.
*** Worry about cleaning the string ****
"""

class Solution:
    def isPalindrome(self, s:str) -> bool:
        arr = []
        # Pre-processing step.
        for i in range(len(s)):
            if s[i].isalpha():
                arr.append(s[i].lower())
        l = len(arr)-1
        r = 0
        if arr:
            while l:
                if arr[l] == arr[r]:
                    l -= 1
                    r += 1
                else:
                    return False
            return True
        return False