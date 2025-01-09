"""
input: List[int]
 |
 -> sparks the creation of the NumArray class, which can handle
    multiple queries of the style:
            sumRange(left: int, right: int)
    which is a class method that can handle that type of
    query.
"""
from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        cur = 0
        self.__prefix = []
        for n in nums:
            cur += n
            self.__prefix.append(cur)
    
    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.__prefix[right] - self.__prefix[left - 1]
        else:
            return self.__prefix[right]