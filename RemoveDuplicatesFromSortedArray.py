from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1,len(nums)):
            if nums[r-1] != nums[r]:
                nums[l] = nums[r]
                l+=1
        return l, nums

# Create an instance of the Solution class
solution = Solution()

# Define the input list
nums = [0,0,1,1,1,2,2,3,3,4]

# Call the removeDuplicates method
k, mod_list = solution.removeDuplicates(nums)

# Print the modified list and the length of unique elements
print("Modified list:", mod_list)
print("Length of unique elements:", k)