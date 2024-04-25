from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        while r < len(nums) - 1:
            if nums[l] == nums[r]:
                nums[r] = '_'
                nums[l] = nums[i]
                l+=1
            r += 1
        print(nums)
        return l

# Create an instance of the Solution class
solution = Solution()

# Define the input list
nums = [0,0,1,1,1,2,2,3,3,4]

# Call the removeDuplicates method
length = solution.removeDuplicates(nums)

# Print the modified list and the length of unique elements
print("Modified list:", nums[:length])
print("Length of unique elements:", length)