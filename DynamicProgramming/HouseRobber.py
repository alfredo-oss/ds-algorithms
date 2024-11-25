"""
* input: [1, 2, 3, 4] # array of houses and their corresponding value of being robbed.

* first question to be asked: can this problem be broken down into sub-problems.

* there are possibly two choices to start:
   - you either start at index 0 or 1

* we have to identify what the recurrence relationship is:
    - in this case we will want the maximum value between the two choices.
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return cache[i]

        return dfs(0)
    


