from typing import List
"""
lets solve this with memoization:
grid : [[0]*cols for i in range(rows)]
* the representation of an invalid square is just as going out of bounds,
  it can be cached just by assignign a 0
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]):
        tarx = len(obstacleGrid)
        tary = len(obstacleGrid[0])
        cache = [[0]*tary for _ in range(tarx)]

        def helperMemo(r, c, tarx, tary, cache):
            if r == tarx or c == tary or obstacleGrid[r][c] == 1 :
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == tarx - 1 and c == tary - 1:
                return 1
            
            cache[r][c] = helperMemo(r + 1, c, tarx, tary, cache) + helperMemo(r, c + 1, tarx, tary, cache)
            return cache[r][c]
        
        return helperMemo(0, 0, tarx, tary, cache)

