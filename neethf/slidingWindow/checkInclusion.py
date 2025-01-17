"""
input: s1: str, s2: str
output: bool

notes:
-----
* we are asked to solve this problem in O(n) time and O(1) space.

* the problem statement gives us a hint of the strings only containing a - z letters

* one way to account for this is to have 2, 26 elements in two different hashmaps accounting for the amount of letters.
    -> and this is one thing to take into account, since you are operating with only 26 letters, and that
       will be THE size of the array for the WHOLE time. Thus, this makes the case for O(1) space.

* these two hashmaps will be backing up our sliding window approach.

* we also need to initialize our matches variable in order to not have to compare all the elements in the hashmaps

solution:
--------
if len(s1) > len(s2):
    return False

s1Count = {}
s2Count = {}
matches = 0

# the first step of initialization is to insert the 26 (a - z) letters into the hashmaps
for i in range(26):
    curChar = char(ord('a') + i)
    s1Count[curChar] = 0
    s2Count[curChar] = 0

# here we are initializing the data structure that will hold the count for the "main string"
# we are also "taking advantage" of the "main" iteration to use account for what we have in the s2 string
for i in range(len(s1)):
    s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0)
    s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)

for i in range(26):
    curChar = char(ord('a') + i)
    if s1Count[curChar] == s2Count[curChar]:
        matches += 1

L = 0
                [we already traversed s1 so, it is not necessary to do it again,
                 here you have to note that len(s1) is non-inclusive, thus its ok
                 to start with this value]
                  |
for R in range(len(s1), len(s2)):
    if matches == 26:
        return True

    s2Count[s2[R]] = 1 + s2Count.get(s2[R], 0)
    if s2Count[s2[R]] == s1Count[s2[R]]:
        matches += 1
    elif s2Count[s2[R]] == s1Count[s2[R]] + 1:
        matches -= 1
    
    s2Count[s2[L]] -= 1
    if s2Count[s2[L]] == s1Count[s2[L]]:
        matches += 1
    elif s2Count[s2[L]] == s1Count[s2[L]] - 1:
        matches -= 1
    L += 1
return False
    
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = {}
        s2Count = {}
        matches = 0

        for i in range(26):
            curChar = chr(ord('a') + i)
            s1Count[curChar] = 0
            s2Count[curChar] = 0
        
        for i in range(len(s1)):
            s1Count[s1[i]] = 1 + s1Count.get(s1[i], 0)
            s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)
        
        for i in range(26):
            curChar = chr(ord('a') + i)
            if s1Count[curChar] == s2Count[curChar]:
                matches += 1
        L = 0
        for R in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            s2Count[s2[R]] += 1 
            if s2Count[s2[R]] == s1Count[s2[R]]:
                matches += 1
            elif s2Count[s2[R]] == s1Count[s2[R]] + 1:
                matches -= 1

            s2Count[s2[L]] -= 1
            if s2Count[s2[L]] == s1Count[s2[L]]:
                matches += 1
            elif s2Count[s2[L]] + 1 == s1Count[s2[L]]:
                matches -= 1
            L += 1
        return matches == 26