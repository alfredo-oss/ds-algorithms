from typing import List
"""
Now, I'm going to solve this with Bottom Up Dynamic Programming
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        prevRow = [0]*cols
        for r in range(rows-1, -1, -1):
            curRow = [0]*cols
            if obstacleGrid[r - 1][cols - 1] == 1:
                curRow[cols - 1] = 0
            curRow[cols - 1] = 1
            for c in range(cols - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                curRow[c] = prevRow[c] + curRow[c + 1]
            prevRow = curRow
        return curRow[0]