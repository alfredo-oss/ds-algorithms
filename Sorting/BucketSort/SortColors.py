from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        # Initializing the counts array
        counts = [0, 0, 0]

        # Filling the counts array by the presence of the colors in the array
        for n in nums:
            counts[n] += 1
        
        # Re-filling the original array
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1
        return nums
