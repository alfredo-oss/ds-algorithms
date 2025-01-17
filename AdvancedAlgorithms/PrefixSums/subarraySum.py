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
"""
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        L, R = 0, 1
        count = 0
        prefix = []
        cur = 0
        for n in nums:
            cur += n
            prefix.append(cur)

        while R < len(prefix) and L < R:
            
            if prefix[R] == k:
                count += 1
                R += 1
                
            elif prefix[R] > k and prefix[R] - prefix[L] == k:
                count += 1
                L += 1
            R += 1

        return count
