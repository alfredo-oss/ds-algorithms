"""
input: s1: str, s2: str
output: bool

notes:
-----
* check if a permutation of s1 is contained in the s2.

example:
-------
*** 
Input: s1 = "abc", s2 = "lecabee"
Output: true

***
Input: s1 = "abc", s2 = "lecaabee"
Output: false


question:
--------
* can i sort the strings?
    -> sorting the strings could mess up the algorithm. you have to take the string just as is.

ideas:
------
what i could do is to initialize a window of size s1 and slide it accross the array. in case the two external pointers
are in the s1 string, I could start an internal search of the subarray, shifting L and R until they cross. If an alert wasnt raised,
return true, else keep searching.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L, R = 0, len(s2) - 1
        for L in range(len(s2) - len(s1)):
            R = L + len(s1)
            while (s2[L] in s1) and (s2[R] in s1) and (L < R):
                R -= 1
                L += 1
                if (s2[L] not in s1) or (s2[R] not in s1):
                    break
            if L + 1 == R and (s2[L] in s1) and (s2[R] in s1):
                return True
        return False    
# This solution wouldnt work because it doesnt take into account if the elements in s2 are unique or
# the amount of times the element is present. The problem is more complex.