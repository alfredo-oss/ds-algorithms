from typing import List

class Solution:
    def firstBadVersion(self, n: int) -> int:

        low, high = 0, n

        while low <= high:
            mid = (low + high) // 2

            if not isBadVersion(mid) and not isBadVersion(mid + 1):
                low = mid + 1
            elif isBadVersion(mid) and isBadVersion(mid + 1):
                high = mid - 1
            else:
                return mid + 1
                 