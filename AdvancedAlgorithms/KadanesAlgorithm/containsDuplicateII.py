"""
int: List[int]
output: bool
------------
We are given an integer array where we are asked 
if at different indices of a subarray of length k, 
we can find the exact same number.
"""
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> int:
        for L in range(len(nums)):
            for R in range(L + 1, min(L + 1 + k, len(nums))):
                if nums[L] == nums[R]:
                    return True
        return False