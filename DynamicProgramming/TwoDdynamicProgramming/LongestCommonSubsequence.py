"""
search space:
    text1 = "cat"
    text2 = "crabt"
a common subsequence: sub sequence that exists in both strings:

example:
--------
    text1 = "cat"
    text2 = "crabt"
    common subsequence = 3

    ---------not sub sequence ------
    text1 = "cat"
    text2 = "tac"
    common subsequence = 1

notes: 
    * subsequences have to be unique
    * keep track of characters in visited (aside from caching)
    * order of charachters matter

recursion :
    i ask: is this character present in this order
    base cases:
        * array already traversed or already visited element return 0 
        * if i find the element in whats left of the array return 1
"""

"""
BRUTE FORCE SOLUTION:
=====================
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(curr, target):
            if curr == len(text1) or target == len(text2):
                return 0
            if text1[curr] == text2[target]:
                return 1 + dfs(curr + 1, target + 1)
        
            return max(dfs(curr + 1, target), dfs(curr, target + 1))
        
        return dfs(0, 0)
"""

"""
TOP DOWN DP SOLUTION:
====================

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def dfs(curr, target, cache):
            if curr == len(text1) or target == len(text2):
                return 0
            if text1[curr] == text2[target]:
                return 1 + dfs(curr + 1, target + 1, cache)
            if (curr, target) in cache:
                return cache[(curr, target)]
            
            cache[(curr, target)] = max(dfs(curr, target + 1, cache), dfs(curr + 1, target, cache))

            return cache[(curr, target)]
        return dfs(0, 0, cache)
"""
"""
BOTTOM UP DP SOLUTION:
======================
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        
        for i in reversed(range(len(dp) - 1)):
            for j in reversed(range(len(dp[0]) - 1)):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
