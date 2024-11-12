from typing import List
from collections import deque

class Solution: 
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visit = set()
        fresh_count = 0
        
        def search(rows: int, cols: int, length: int, visit, queue, grid, fresh_count) -> int:
            visit = visit
            queue = queue
            length = length
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for dr, dc in neighbors:
                        if (min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 0 or grid[r + dr][c + dc] == 2):
                            continue
                        queue.append((r + dr, c + dc))
                        visit.add((r + dr, c + dc))
                        fresh_count -= 1
                length += 1
            return length - 1, fresh_count

        # search for rotten fruit
        # i will first append all rotten orag\nges to the queue which will initialize the search
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visit.add((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                
        if queue and fresh_count > 0:
            length, fresh_count = search(ROWS, COLS, 0, visit, queue, grid, fresh_count)
            if fresh_count == 0:
                return length
            elif length == 0:
                return - 1
        elif queue and fresh_count == 0:
            return 0
        else: 
            return - 1
