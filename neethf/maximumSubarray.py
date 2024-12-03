"""
input -> nums: list[int]
output -> sum: int
subarray: contiguous sequence of elements. (we cant skip)
example:
--------
nums = [-2,1,-3,4,-1,2,1,-5,4]
"""
# Kadane's Algorithm
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        curSum = 0
        
        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(curSum, maxSum)
        return maxSum
