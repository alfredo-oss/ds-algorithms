from typing import List

class Solution:
    def helperBinary(self, nums: List[int], target: int) -> bool:

        L, R = 0, len(nums)-1

        while L <= R:
            mid = (L + R)//2

            if nums[mid] < target:
                L= mid+1
            elif nums[mid] > target:
                R = mid-1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        L_m, R_m = 0, len(matrix)-1

        while L_m <= R_m:

            mid_m_x, mid_m_y = ((L_m + R_m)//2), 0

            if self.helperBinary(matrix[mid_m_x], target):
                return True
            else:
                if matrix[mid_m_x][mid_m_y] < target:
                    L_m = mid_m_x + 1
                elif matrix[mid_m_x][mid_m_y] > target:
                    R_m = mid_m_x - 1
        return False
