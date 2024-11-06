from typing import List

# The whole purpose of this approach is to not count (1's) that I already visited 

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, r, c, visited):
            ROWS, COLS = len(grid), len(grid[0])
            # definition of base cases
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == "0"):
                return
            
            visited.add((r,c))
            dfs(grid, r + 1, c, visited)
            dfs(grid, r - 1, c, visited)
            dfs(grid, r , c + 1, visited)
            dfs(grid, r , c - 1, visited)

            return visited
        
        def search(grid, visited):

            ROWS, COLS = len(grid), len(grid[0])
            icount = 0

            for row in range(ROWS):
                for col in range(COLS):
                    if (row, col) not in visited and grid[row][col] == "1":
                        dfs(grid, row, col, visited)
                        icount += 1

            return icount
        
        return search(grid, set())

            