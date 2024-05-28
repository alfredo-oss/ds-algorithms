"""
Given an integer array nums, return true if any value 
appears more than once in the array, otherwise return
"false".
-----------------
In this case, I have to ask my self:
- Does the current number (position) repeats along the array?
- To achieve that I need two pointers:
    ** l : will keep track of the current number.
    ** r : will go and browse in the array.
  The more straightforward way is creating a linked for loop
  with one pointer referencing the "current" value and the other
  pointer browsing for duplicated values.

- Since we are looking for ANY duplicated values, one occurrence 
  is enough to return the corresponding boolean.
"""
from typing import List

class Solution:
    def hasDuplicate(self, nums: List) -> bool:
        for l in range(len(nums)):
            print(f"Left: {l}")
            for r in range(l+1, len(nums)):
                print(f"Right: {r}")    
                if nums[l] == nums[r]:
                    return True
        return False
solution = Solution()
test = [1, 2, 3, 4]
print(solution.hasDuplicate(test))