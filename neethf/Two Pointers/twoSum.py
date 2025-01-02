"""
input: List[int] (sorted array of numbers), int (integer indicating the target sum)
output: List[int] (containing the 2 indexes of the numbers that sum up to the target number) 
!! The output has to be 1-indexed

notes:
-----
* my array is sorted, thus i know that the right most element is the biggest element and the 
  left most element is the smallest element.
* when i sum two elements, the sum can be either greater or smaller than the target number.
* if the sum is bigger then I shift my R pointer to the left because there is no way that I can achieve a smaller sum
  shifting my L pointer since every sum would be bigger than the current sum.
* if the sum is smaller i do the opposite with the left pointer.
* the only case that's left is when the sum is equal, which in that case I will just return the L, R pointer
"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            else:
                return [L + 1, R + 1]
            