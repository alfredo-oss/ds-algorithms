from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # We initialize the left and right pointer to be able to travel the array that contains the different k's
        res = r

        while l <= r:
            k = (l + r) // 2 # Since we are iterating on the array that contains the possible k's. k will play a similar role to what "mid" does in binary search.
            hours = 0

            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
            