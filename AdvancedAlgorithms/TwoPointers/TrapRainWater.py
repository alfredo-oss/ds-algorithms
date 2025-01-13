"""
input: List[int] # an array of integers representing the heigth of a retaining wall at point height[i]
output: int # the maximum area of water that can be trapped between the walls

example: 
-------
Input: height = [0,2,0,3,1,0,1,3,2,1]
                     2   2 3 2 = 9
Output: 9

notes:
-----
* an approach could be to sum area by area

   #
 #|#
 #|#
 ---
* in order to sum an area we need to know what the maximum height is at each border of the array
* an area for catching water is defined by:
    1) a block in the middle of two walls that is smaller than the two walls
"""
class Solution:
    def trap(self, height: list[int]) -> int:
        L, R = 0, len(height) - 1
        res = 0
        maxLeft , maxRight = height[L], height[R]
        while L < R:
            if height[L] < height[R]:
                L += 1 
                maxLeft = max(maxLeft, height[L])
                res += maxLeft - height[L]
            else:
                R -= 1
                maxRight = max(maxRight, height[R])
                res += maxRight - height[R]
        return res
    