from typing import List
from heapq import heapify, heappop
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        auxRes = []
        auxPoints = []
        for x, y in points:
            auxRes.append((math.sqrt(((0-x)**2 + (0-y)**2)), x, y))
        
        heapify(auxRes)

        for i in range(k):
            _, x, y = heappop(auxRes)
            auxPoints.append([x,y])
        return auxPoints