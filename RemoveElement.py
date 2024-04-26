from typing import List

class Solution:
    def RemoveElement(self, val: int, nums: List[int]) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l, nums
    
solution = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
k , mod_list = solution.RemoveElement(val,nums)

print(f"Unique Values: {k}, Modified List: {mod_list}")
