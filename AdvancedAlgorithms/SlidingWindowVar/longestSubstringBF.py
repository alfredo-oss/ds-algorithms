"""
given the an str find the length of the longest substring without duplicate characters.
input: str
output: int

notes:
------
i think this could be solved with two pointers and a recurrence relationship, with each sequence being reset once we find a character that is already present in the sequence.
1) L, R pointer (L will be reset once we find a duplicated character), R will traverse the whole string.
2) for each element present in the string
    a) IF the element is NOT in the auxiliary set
        b) that element will be added to an auxiliary set
        c) the length will be equal to R - L + 1 and maxLen = (R - L + 1, maxLen)
    d) IF the element is in the auxiliary set
        e) then we reset the auxiliary set
        f) we reset the L pointer
        f) we add the element to the auxiliary set
        g) we calculate the maxLen
3) we return maxLen
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        L, maxLen = 0, float("-inf")
        auxSet = set()
        for R in range(len(s)):
            if s[R] not in auxSet:
                auxSet.add(s[R])
                maxLen = max(R - L + 1, maxLen)
            else:
                auxSet = set()
                L = R
                auxSet.add(s[R])
                maxLen = max(R - L + 1, maxLen)
        return maxLen
