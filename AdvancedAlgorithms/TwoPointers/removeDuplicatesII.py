"""
input:  List[int] (the array is sorted in increasing order)
output: int (the number of resulting elements after cleaning the duplicates), List[int] (the array without the extra duplicates)

example:
--------
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

what are we trying to achieve here?
-----------------------------------
* we need to remove duplicates from the array. the definition of duplicate here variates a little bit. for an element to be a duplicate
  it has to appear more than 2 times in the array.
* if we find the same element for the 3rd time, we will need to replace it with the next distinct element that we find. since the pointer that
  went to look for the next distinct element could have gone very far in the array, the Sliding Window option does not hold here.
* we need to hold the count in an external variable count.

# 1st iteration
Input: nums = [0,0,1,1,1,1,2,3,3]
              ||
              LR  --> L == R then k + 1, because we already know we have a lenght 2 resulting array
                    --> count += 1 because we found the same element twice 
                    --> R += 1 we keep moving
"""     
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 0
        while R < len(nums):
            count = 1 # this count will always initialize when a distinct element is found
            while R + 1 < len(nums) and nums[R] == nums[R + 1]:
                count +=1
                R += 1
            for _ in range(min(2, count)):
                nums[L] = nums[R]
                L += 1
            R += 1 # this last shift is to be able to start at the following distinct character
        return L