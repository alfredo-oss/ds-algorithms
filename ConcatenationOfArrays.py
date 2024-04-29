from typing import List

class Solution:
    def arrayConcat(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None] * (2 * n)

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        
        return ans

solution = Solution()
arr = [1,2,1]
output_list = solution.arrayConcat(arr)
print(f"Output:{output_list}")