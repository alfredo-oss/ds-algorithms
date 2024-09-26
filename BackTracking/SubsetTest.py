from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) # this line will append each Leaf Node
                return
            
            # decision to include nums[i]
            subset.append(nums[i]) #represents the green line path of adding the evaluated element to the objective list
            dfs(i + 1) # we proceed to call the following element on the array

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res