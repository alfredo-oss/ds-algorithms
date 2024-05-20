"""
val = 2
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_] k = 5

I have to look for numbers that do not correspond to 2, if I find a two, I need a left pointer that tells me where that 2 is, and a right pointer that goes and looks for the next value that is not 2.

"""
from typing import List, Tuple
class Solution:
    def RemoveElement(self, arr: List[int], val:int) -> Tuple[List[int], int]:

        l = 0

        for r in range(len(arr)):
            if val != arr[r]:
                arr[l] = arr[r]
                l += 1
        return arr, l

solution = Solution()
nums = [0,1,2,2,3,0,4,2]
print(solution.RemoveElement(nums, 2))
