"""
for each iland we need to return the number of cells traversed assuming
that each cell is 1x1.

*first i need to look for a spot where is "valid" to start investigating. which could be considered
 brute-force but its not really necessary.
* each time i find a valid spot, we will initialize a temporary variable to 0.
  it is necessary to return the area of that spot to a temporary variable that 
  will be added to an auxiliary array where we will get the maximum value, that being
  the area of the Island.
* this could be achieved with DFS and BFS, lets start with DFS.
"""
from typing import List
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(grid, r,c):
            if (min(r,c) < 0) or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            count = 1
            count += dfs(grid, r + 1, c)
            count += dfs(grid, r, c + 1)
            count += dfs(grid, r - 1, c)
            count += dfs(grid, r, c - 1)
            return count
        aux = []
        for r in range(ROWS):
            for c in range(COLS):
                area = 0
                if grid[r][c] == 1:
                    area = dfs(grid, r,c)
                    aux.append(area)
        return max(aux) if aux else 0
    
"""
Now, lets implement it with BFS.
For the case of BFS, the key is to only add valid options in all levels.
When each option is added then we increment the count of the Island.

grid=[[1,1,0,0,0],
      [1,1,0,0,0],
      [0,0,0,1,1],
      [0,0,0,1,1]]
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(grid, r, c):
            count = 1
            ROWS, COLS = len(grid), len(grid[0])
            positions = [[1, 0], [0, 1], [-1, 0], [0, -1]] 
            queue = deque()
            queue.append((r, c))
            grid[r][c] = 0
            while queue:
                row, col = queue.popleft()
                for dr, dc in positions:
                    rm, cm = row + dr, col + dc
                    if rm < ROWS and rm >= 0 and cm < COLS and cm >= 0 and grid[rm][cm] == 1:
                        queue.append((rm, cm))
                        grid[rm][cm] = 0
                        count += 1
            return count
        
        aux = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = bfs(grid, r, c)
                    aux.append(res)
        return max(aux) if aux else 0