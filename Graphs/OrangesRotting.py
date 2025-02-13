"""
We are given a 2-D matrix grid. Where each cell can have one of three possible values.
-> 0 : an empty cell
-> 1 : a fresh fruit
-> 2 : a rotten fruit

Every minute, if a fruit is horizontally or vertically adjacent to a rotten fruit, then the 
fresh fruit also becomes rotten.
 --> this means that we are not allowed to move either vertically or horizontally.
 --> a catch here is that we cant either assume that just because of the fact of 
     finding a rotten fruit a minute would have elapsed.
     ---> In this case the minutes represent the levels of decisions
--> the grid will always the composition of:
    -> rows <= 5
    -> cols <= 5
--> the "catchy" case is when you have two disconnected areas where infection can be
    induced.
    grid = [[2,1,1,0,0], --> In this case we would take the max of the two cases
            [0,1,0,0,0],     because technically the oranges would be rotting in
            [0,0,2,1,1]]     parallel.

--> now, the other interesting case is the one where there is not a way to rot the whole
    grid:
    grid = [[1,1,1,0,0], --> an intuitive way to know that you didnt rotten all the fruit
            [0,1,0,0,0],     is by counting the total number of fresh fruit at the beginning
            [0,0,2,1,1]]     and comparing it to the amount of fresh fruits at the end.
                             if the amount is 0 then we return the minutes it took us to
                             rotten all the fruit [which could be a "maximum" relationship,
                             so, we make sure that we always mantain the maximum value]

--> Test case:
    grid=[[2,1,1],
          [1,1,1],
          [0,1,2]]

--> I need to recollect and add all the places where there are rotten fruits.

"""
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid:List[List[int]]) -> int:
        if not grid:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        def countFreshFruit(grid):
            nonlocal ROWS
            nonlocal COLS
            fresh_fruit = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:
                        fresh_fruit += 1
            return fresh_fruit
        
        def bfs(grid, r, c):
            nonlocal ROWS
            nonlocal COLS
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            queue = deque()
            queue.append((r, c))
            grid[r][c] = 0
            minute = 0
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc
                        if (min(new_row, new_col) >= 0) and new_row < ROWS and new_col < COLS and grid[new_row][new_col] == 1:
                            queue.append((new_row, new_col))
                            grid[new_row][new_col] = 0
                minute += 1
            return minute - 1
        max_minute = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    max_minute = max(max_minute, bfs(grid, r, c))
        final_fresh = countFreshFruit(grid)
        return max_minute if not final_fresh else -1