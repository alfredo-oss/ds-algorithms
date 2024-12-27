"""
Input: nums = [0,3,2,5,4,6,1,1]

Output: 7 -> this represents the longest consecutive sequence of elements

notes:
-----
* the a consecutive sequence is formed only if n is greater than n - 1 by 1 unit.
* the time complexity of the algorithm has to be O(n).
* the sequence does not have to be in order.

questions:
----------
* can we built in sort the array?
* maybe i can have two pointers that start on each side of the array until a condition is met. One moves to the left and another one moves to the right.
    -> in this case you would encounter that maybe the sequence starts in the middle. then you would have to travel all the way to the middle to be able to start even analyzing the sequence, thus it wouldnt be O(n). but I guess you could even go 100 times through the same array
       and it would still be O(n). 
solution:
--------
* one thing that i didnt know is that you can actually transform an array into a set() class just by calling it.
    -> this allows you to query if n-1 is present in the set. If not, it means that you found the possible start of a sequence and you can initialize a variable length.
    -> while the n + lenght(length starting at 1) is present, length will increase +1
    -> after the condition is not met, we check the recurrence relation with maxLen = max(maxLen, length)
    -> after every number in the set is analyzed, we return the length
    (!) just to be sure we will take the case that if we receive an empty array, we will return 0.
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        maxLen = float("-inf")
        for num in numSet:
            if (num - 1) not in numSet:
                length =  1
                while (num + length) in numSet:
                    length += 1
                maxLen = max(maxLen, length)
        return maxLen