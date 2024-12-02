"""
valid anagram:
- for a pair to be an anagram they have to have letter1 == letters2
s = "anagram"
t = "nagaram"
- if we sort the elements the solution would be much faster : sort
1) sort
2) for each element 
"""
"""
# BRUTE FORCE
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s = sorted(s)
            t = sorted(t)
            for i in range(len(s)):
                if s[i] != t[i]:
                    return False
            return True
        else:
            return False
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            countT = {}
            countS = {}

            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
            return countT == countS
        else:
            return False