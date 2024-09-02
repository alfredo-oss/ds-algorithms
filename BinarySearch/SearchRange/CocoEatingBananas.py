from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # We initialize the left and right pointer to be able to travel the array that contains the different k's
        res = r

        while l <= r:
            k = (l + r) // 2 # Since we are iterating on the array that contains the possible k's. k will play a similar role to what "mid" does in binary search.
            hours = 0

            for p in piles: # On each "while" iteration we evaluate how many hours it takes us to eat all the bananas 
                hours += math.ceil(p/k)
            
            # This is the condition that will update our pointers
            if hours <= h: # if hours is < than "h" that means that we could find a smaller value for k. The same goes for when hours is = k but in that case, we would probably meet the outer while constraint and the loop would break.
                res = min(res, k) # we update the result in the "possible" scenario evaluation.
                r = k - 1 # since we still have smaller values to evaluate we subtract our right pointer.
            else: # This evaluation statement takes into account the case when "k" was too small and the hours it took to eat all the bananas is greater than the threshold "h".
                l = k + 1 # since the "k" we chose previously was too small, we need to update the k selection to a greater value.
        
        return res # finally, we return the result.
            