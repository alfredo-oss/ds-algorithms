"""
contains duplicate: 
input: array of integers
output: boolean -> true if there is at least one duplicate.
                   false if every element is distinct.
example:
---------
    [1, 2, 3, 1] -> true
    [1, 2, 3, 4] -> false

solution:
---------
 dict[element] = #count
 if dict[element] == 2:
    return True
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        aux = {}
        for element in nums:
            if element not in aux:
                aux[element] = 1
            else:
                aux[element] += 1
                return True
        return False