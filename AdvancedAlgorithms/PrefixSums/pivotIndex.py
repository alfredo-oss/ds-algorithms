"""
input: List[int]
-> Given this array we have to calculate the pivot index.
-> A pivot index is the index of the array where the sum of the array (strictly to the left, not including the index)
   strictly to the left is equal to the sum of the index strictly to the right.

output: int -> left most pivot index (this gives us a hint that we could optimize the algorithm by iterating from the left edge)
example (1):
------------
Input: nums = [1,7,3,6,5,6]
                     |
                   [pivot
                    index]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

example (2): # this is the catchy case.
------------
Input: nums = [2,1,-1]
               |
             [pivot
              index]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

solution:
---------
-> the first thing here would be to calculate the prefix-sum of the array:
-> Im assuming for now to optimize as much as possible but there are no time or space restrictions.
# create prefix_sum array
if not nums:
    return -1

cur = 0
sum_array = []
for i in range(len(nums)):
    cur += i
    sum_array.append(cur)

leftSum = 0
rightSum = 0
for index in range(len(sum_array)):
    if leftSum == rightSum:
        return index
return -1

I didnt came up with the most elegant solution but it worked!
"""
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        cur = 0
        sum_array = []
        for i in range(len(nums)):
            cur += nums[i]
            sum_array.append(cur)
        
        for index in range(len(sum_array)):
            if index == 0:
                leftSum = 0
            else:
                leftSum = sum_array[index - 1]
            if index == len(nums) - 1:
                rightSum = 0
            else:
                rightSum = sum_array[len(sum_array) - 1] - sum_array[index]
            if leftSum == rightSum:
                return index
        return -1
    
"""
There is actually a more elegant way to solve this problem. It reduces the memory usage but not the time
complexity. And that is because instead of calculating an auxiliary array holding the prefix-sum we can
directly calculate the total sum.
So, at any point in time and in order to consider the case of the leftSum = 0, we will need to traverse the 
whole array.
    [1 ,2 ,3 ,4 ,5]
     |           |
  [pivot       [total
   index]        sum] -> there is a pre-work of calculating the [total sum]

at x point in the array:
------------------------   
leftSum: will increment with the traversal of the main pointer
rightSum = totalsum - arr[pivotIndex] - leftSum

elegant solution:
-----------------
class Solution:
    def pivotIndex(self, nums: int) -> int:
        leftSum = 0
        totalSum = sum(nums) # O(n)
        for index in range(len(nums)):
            rightSum = totalSum - nums[index] - leftSum
            if leftSum == rightSum:
                return True
            leftSum += nums[index]
        return False   
"""
class Solution:
    def pivotIndex(self, nums: int) -> int:
        leftSum = 0
        totalSum = sum(nums) # O(n)
        for index in range(len(nums)):
            rightSum = totalSum - nums[index] - leftSum
            if leftSum == rightSum:
                return True
            leftSum += nums[index]
        return False   