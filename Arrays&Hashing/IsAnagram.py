"""
First I will assume that the two strings s and t are going to be simple strings without spaces...is that a fair assumption?
The anagram does not analize the position of the elements of the string, it analyzes that both strings have exactly the same characters.
What I could do is to choose either string, start at index 0 take that letter and ask "Is "s" present in the following string?"
To answer that question I need to go over the other string and check if the string is there.
If yes is the answer I can move on to the next element in the chosen string, else, I could declare that the letter is not there and 
by default the anagram condition would not be met. 
-------------------
How do i check that the string is present?
I could generate a counter that adds +=1 any time it finds a matching element.
Then at the end if that counter matches the length of the chosen string then we can
return true, else we return false. --> That does not work because it goes bananas when you have a letter present two times in the array
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for l in s:
            c = 0
            for r in t:
                if l == r:
                    c +=1
            if c == 0:
                return False
        return True

solution = Solution()
s = "jar"
t = "jam"
print(solution.isAnagram(s,t))
                