"""
input: List[str] (upper-case english letters), k: int (how many replacements i can make)
ouput: int (lenght of the longest substring(consecutive set of characters) where there is only one distinct character, which I assume that is the same as having the same repeated character)

example (1):
------------
Input: s = "XYYX", k = 2
Output: 4

example (2):
------------
Input: s = "AAABABB", k = 1

Output: 5

notes:
------
We will cover this from a point of view that makes sense:
    1) we will hold the count of a character in a HashMap because that count can be constantly increasing as we traverse the array.
    2) we will hold a maxf variable that will contain the maximum character frequency at any point in time
    3) we will calculate the length of the current window versus the current maxf and see if we can cover the difference with our wildcard k.
    4) while the condition is not met, we will shift the pointer.
"""
from typing import List

class Solution:
    def characterReplacement(self, s: List[str], k: int) -> int:
        count = {}
        L, res = 0, 0
        maxf = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0) 
            maxf = max(maxf, count[s[R]])
            while (R - L + 1) - maxf > k:
                count[s[L]] -= 1 # we subtract 1 because that element is not supposed to be present in our current window
                L += 1
            res = max(R - L + 1, res)
        return res