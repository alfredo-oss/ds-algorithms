from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def helperDfs(grid, r, c, visited, count):
            ROWS = len(grid)
            COLS = len(grid[0])
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == 0):
                return 
            visited.add((r,c))
            count.append(1)
            helperDfs(grid, r + 1, c, visited, count)
            helperDfs(grid, r - 1, c, visited, count)
            helperDfs(grid, r , c + 1, visited, count)
            helperDfs(grid, r , c - 1, visited, count)

            return visited, sum(count)

        def search(grid, visited):
            ROWS = len(grid)
            COLS = len(grid[0])
            carray = []
            for row in range(ROWS):
                for col in range(COLS):
                    count = [0]
                    if (row, col) not in visited and grid[row][col] == 1:
                        visited, count = helperDfs(grid, row, col, visited, count)
                        carray.append(count)
            if carray:
                return max(carray)
            else: 
                return 0 
        return search(grid, set())