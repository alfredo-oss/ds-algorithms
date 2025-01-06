"""
input: List[int] (an array of integers containing the elements that will participate in the sum)
output: List[List[int]] (the output is a list containing the list of elements(triplets) that sum up to 0)
notes:
------
* we should be aiming for an O(n^2) time complexity solution and O(1) extra memory[the output is not considered in the memory complexity].
Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
** if the output contains lists of 3 elements. that means that we need three pointers.
** the output should not contain any duplicate triplets, which considers the actual elements, not the indexes
--------------------------------
[-1,0,1,2,-1,-4]
  k L R
  * One of the pointers will iterate sequentially over the entire array (k).
    -> that element will be appended to the list, now L, R need to look for the rest of combinations (two elements)
       that will satisfy the 0th condition.
    -> whenever we perform the sum, the result can be greater or smaller.
            -> if the result is greater, between the L and R pointer we want to keep the smallest value, and
               shift the greater value. (this entirely depends on how we set the condition)
    -> there is no need for swapping elements with the element at the 0-th index which was my first idea. the catch is simple
       every traversed element by the "main/third" pointer does not need to be considered again by the L pointer in this case,
       thus, L will always start at ("main/third" + 1)

helper:
------
* A very valid question here is if you could sort the array, and the answer is yes, you can.
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                curSum = a + nums[L] + nums[R]
                if curSum > 0:
                    R -= 1
                elif curSum < 0:
                    L += 1
                else:
                    res.append([a, nums[L], nums[R]])
                    L += 1 # inner loop needs to make progress anyway
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1 # "inner loop" has to make progress somehow
        return res
