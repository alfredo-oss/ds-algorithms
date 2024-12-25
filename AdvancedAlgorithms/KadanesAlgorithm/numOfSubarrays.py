"""
input: arr: List[int], k: int, threshold: int
output: res: int
notes:
------
** for each analyzed sub-array you need to calculate the average 
   of the sub-array which is a float. **
** this problem has a little bit of a difference compared to the normal sliding window duplicate because here we are
   accounting just for arrays of length 3, no more, no less. so, thats where the caveat is.

solution:
---------
"""
from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0

        for r in range(k-1, len(arr)):
            sum = 0
            for i in range(l, r + 1):
                sum += arr[i]
            if sum/k >= threshold:
                res += 1
            l += 1
        return res