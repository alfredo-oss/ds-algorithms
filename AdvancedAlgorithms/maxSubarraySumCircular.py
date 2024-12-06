"""
input: List[int]
output: int

notes
-----
- a circular array means that the end of the array is connected to the beggining.
    - there are three key definitions to the circular subarray:
        next = nums[(i + 1)%n]
        prev = nums[(i - 1)%n]
        curr = nums[i]
- keep the reference as defined
- what is the condition till we iterate through?
- we dont have to sum prev just keep track of it 
example:
--------
[5,-3,5]

simple solution (not circular):
-------------------------------
maxSum = float(-inf)
curSum = 0
i = -1
prev = 0
next = 1
while prev != next:
    prev = nums[(i - 1)%n]
    next = nums[(i + 1)%n]
    curSum = max(curSum, 0)
    curSum += next 
    maxSum = max(curSum, maxSum)
    i += 1
return maxSum

modifications:
--------------
- loop in a circular way

restrictions:
-------------
-> we cant overlap pointers!
    -> which means that somehow we need to keep track of our left and right pointers.
"""
from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in range(len(nums)):
            total += nums[n]
            curMax = max(nums[n], curMax + nums[n])
            curMin = min(nums[n], curMin + nums[n])
            globMax = max(curMax, globMax)
            globMin = min(curMin, globMin)
        return max(globMax, total-globMin) if globMax > 0 else globMax
        