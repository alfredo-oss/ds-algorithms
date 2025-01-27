"""
input: List[int] # represents a list of integers
output: int # returns the integer that is repeated the most times

notes:
-----
-> solving the problem without modifying the array and using
   only constant space is a must (can't create any other
   data structures)

-> no sorting
* consider that the elements ARE in range [1, n], if they were unique
  that range should be present.

"""
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]):
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow