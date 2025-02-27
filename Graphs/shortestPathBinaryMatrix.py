from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visit = set()
        queue.append((0,0))
        visit.add((0,0))
        length = 1
        

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                neighbors = [ (0,1), (0,-1), (1,0), (-1,0), (-1,-1), (-1,1), (1,1), (1,-1)]

                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        return -1