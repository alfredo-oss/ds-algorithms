class Solution:
    def longestConsecutive(self, s: str) -> int:
        L = 0
        res = 0
        charSet = set()

        for R in range(len(s)):
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            charSet.add(s[R])
            res = max(R - L + 1, res)
        return res