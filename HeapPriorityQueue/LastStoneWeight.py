from typing import List
from heapq import heappop, heapify, heappush

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            first = heappop(stones)
            second = heappop(stones)

            if second > first:
                res = second - first
                heappush(stones, -res) # since we are dealing with a minHeap with negative values

        if len(stones):
            return abs(stones[0]) # since we are dealing with negative values we return the absolute value of the last element in case that it exists
        return 0
            
            