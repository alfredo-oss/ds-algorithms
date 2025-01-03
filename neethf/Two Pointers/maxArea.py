"""
input: List[int] (an array of integers, where the elements represent countiguos bars of heigth arr[i])
            -> the first bar i=0 will have height=arr[i]
output: int (the max area that two bars can create)
            -> where we are maximizing:
                    1) the height of the LEFT bar
                    2) the height of the RIGHT bar
                    3) and the distance between the two
notes:
------
* Since what we are filling is water, the max area can only be so high as
  the smallest bar.
  maxArea = min(LEFT, RIGHT) * R - L 
* I'm assuming that it is a constraint to pick two different bars. Thus, L and R pointer need to be started at different positions.

pointer-shifting logic:
----------------------
*  examples: 
        *) Input: height = [1,7,2,5,4,7,3,6]
                              L           R -> (these are the positions that contain the largest area)
           Output: 36 = (7 - 1) * 6

* now, you can maximize your base by starting the pointers at both ends of the array:
            [1,7,2,5,4,7,3,6]
             L             R
    
* what's the update logic for L?
    if arr[L] <= arr[R]:
        L += 1 (Because you want to stay with your "highest" option)
    else:
        R -= 1

    -> [1,7,2,5,4,7,3,6]
          L           R

* at the beggining of each iteration you need to calculate the current area and compare it to get the maxArea
"""
from typing import List

class Solution:
    def maxArea(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        maxArea = 0
        
        while L < R:
            maxArea = max(maxArea, (min(nums[L], nums[R]) * (R - L))) 
            if nums[L] <= nums[R]:
                L += 1
            else:
                R -= 1
        return maxArea