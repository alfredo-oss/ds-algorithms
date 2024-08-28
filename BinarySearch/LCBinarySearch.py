from typing import List

class Solution:
    def search(self, nums: List, target: int) -> int:
        # We initialize the base pointers
        L, R = 0, len(nums)-1

        while L <= R:
            # mid has to be calculated inside the loop because the pointers will be dynamically changing
            mid = (L + R) // 2

            if target > nums[mid]:
                L = mid + 1
            elif target < nums[mid]:
                R = mid - 1
            else:
                return mid
        return -1
                

