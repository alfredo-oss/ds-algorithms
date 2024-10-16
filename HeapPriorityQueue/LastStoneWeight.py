from typing import List
from heapq import heappop, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)

        
            
            