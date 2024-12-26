"""
input: List[int]
output: int

notes:
-----
input: target = 7, nums = [2,3,1,2,4,3]
the way to approach this problem is through a sliding window:
-> L, R pointer
-> length variable (this will store the value of the current sum)
How this will work:
    1) we have an R pointer that will iterate over all the elements of the array. (could be built with a for loop/where we would 0-index the pointer)
    2) per each iteration we will add the current element to a sum auxiliary variable
    3) while the sum is met, we will find the minimum length with a recurrent comparison R-L+1, length (which indicates the comparison of the current length and the previous length)
        A) within this same while loop we would test if the total sum is still met if the L pointer is increased by 1.
    4) finally if the length is == float("inf") we return 0 else we return the desired length
"""
from typing import List

class Solution:
    def minSubArrayLen(self, nums: List[int], target: int) -> int:
        L, total = 0, 0
        length = float("inf")
        
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L += 1

        return 0 if length == float("inf") else length