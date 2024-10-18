from typing import List
from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [s*-1 for s in nums]
        heapify(nums)
        for _ in range(k-1):
            heappop(nums)

        res = heappop(nums)
        if res > 0:
            return -res
        return -res