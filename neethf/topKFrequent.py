"""
input: nums: List[int], k: int
output: res: List[int]
* The fact that we need to account for a unique number being present a certain amount of times,
  makes this problem very suitable for using a HashMap where we can hold accountability for each
  unique element.
* In the worst case we would have to traverse the HashMap another time with each element having a 
  presence of 1, which would create time complexity of 2*n which ends up being O(n) because we don't
  care about constants.
"""
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        haset = {}
        for n in nums:
            haset[n] = 1 + haset.get(n, 0)
        aux = []
        for nm, count in haset.items():
                aux.append((count, nm))
        aux.sort()
        res = []
        while len(res) < k:
             res.append(aux.pop()[1])
        return res