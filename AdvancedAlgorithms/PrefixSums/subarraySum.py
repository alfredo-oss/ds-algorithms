"""
input: list[int], int # a list of integers and a target k
output: int # the amount of subarrays that sum up to k
notes:
------
* a subarray is a contiguous non-empty sequence of elements within an array,
    -> which means we can assess the amount of combinations in one pass.
        O(n)

example:
-------
Input: nums = [1,2,3], k = 3
Output: 2

-> lets see what we could do here:
    lets assume we do the pre-work of getting a prefix sum of the same array, because
    until now we do not have restrictions on memory usage:
    
    -> prefixSum = [1, 3, 6]
                    |
                   [k]    
    
    -> secondly we could start a pointer that traverses the prefixSum array and asks
       is this element, (resulting from a consecutive sum of elements) EQUAL to the 
       target?

example (2):
-----------
Input: nums = [1,1,1], k = 2
Output: 2

    -> prefixSum = [1, 2, 3]
                    L     R
    here is the catch, R will traverse looking for the element, but if
    R gets too big, then we will subtract L and shift it to see if the 
    following subarray makes the target.

edge case (3):
--------------  
Input: nums = [5, 4, 1, 1, 1, 1], k = 2
Output: 2

    -> prefixSum = [5, 9, 10, 11, 12, 13]
                               L       R
                    count = 3
    L should not shift unless it is used to reach the target number

Brute Force O(n^2):
------------
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)): # we start at i because we know the sub-array has to be contiguous
                sum += nums[j]
                if sum == k:
                    count += 1
        return count

Optimized O(n) sum:
-------------------
This solution has a catch, which is that you can't precompute the prefixes for all the elements in the array.
The intuition is the following:
    [1, -1, 1, 1, 1, 1]
For each element we would ask:
    - how many prefixes can we chop from consideration to achieve
      the target?
      -> A prefix can only be chopped if it meets the difference between
         the current sum and the target value.
This brings me to the next big concept, which is how do we know how many
prefixes meet this condition. Well, we can achieve this by performing lookups
to a hashmap, which will hold historical prefixes counts.
    -> It is necessary to initialize the hashmap with a 0 : 1 count in case one single 
       element meets the target value.
"""                     
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        preMap = { 0 : 1}
        diff = 0
        curSum = 0
        res = 0
        for n in nums:
            curSum += n
            diff = curSum - k
            res += preMap.get(diff, 0)
            preMap[curSum] = 1 + preMap.get(curSum, 0)
        return res
