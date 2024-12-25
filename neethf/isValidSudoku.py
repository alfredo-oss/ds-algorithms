"""
input: List[List[int]] # 9 x 9 Sudoku Grid
ouput: bool # Indicating if the grid is a valid or invalid Grid
notes:
------
For a grid to be valid (in this case) we need to evaluate only on the filled cells, the following conditions:
1) each row must contain the digits 1-9 without repetition.
2) each column must contain the digits 1-9 without repetition.
3) each of the 9 sub-boxes must contain digits 1-9 without repetition. (the sub-boxes are predefined)

considerations:
---------------
* if a row or column is invalid we should return false.
* the search has to be exhaustive
* for a current cell (with a value as key) we need to analyze
  if in the colum, row and current sub-grid the value is present more than once.
* we should also take advantage of that search effort and see if the current or comparing values are in the 1-9
  range.
*sub-grid representation*

1st-grid: grid[0:3][0:3]
2nd-grid: grid[0:3][3:6]
3rd-grid: grid[0:3][6:9]

depending on where the cell is the search needs to happen at the corresponding sub-grid.
example:
-------
1) we need to iterate through the entire grid but, we can cache the behaviour for a row, column or sub-grid.
2) if a valid value is encountered twice in the same key, then the loop should break and return the corresponding boolean value.
3) we dont need to iterate through each valid element: row, col, sub-grid. We just need to cache the values and if we encounter them twice then we stop.
4) how do we cache the key for the sub-grid?
   -> for row
          for col
              lets suppose we are at cell grid[0][5]:
                    how do we align it with a sub-grid key?
                    -> this element should be asociated with the 2nd-grid: grid[0:3][3:7]:
                       and we could cache them as a list
                       -> the key here is the arithmetic of the col or row: and the arithmetic will be constant for row//3 and col//3

                [["8","3",".",".","7",".",".",".","."],
                 ["6",".",".","1","9","5",".",".","."],
                 [".","9","8",".",".",".",".","6","."],
                 ["8",".",".",".","6",".",".",".","3"],
                 ["4",".",".","8",".","3",".",".","1"],
                 ["7",".",".",".","2",".",".",".","6"],
                 [".","6",".",".",".",".","2","8","."],
                 [".",".",".","4","1","9",".",".","5"],
                 [".",".",".",".","8",".",".","7","9"]]
"""
from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        subGridSet = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in rowSet[row] or board[row][col] in colSet[col] or board[row][col] in subGridSet[row//3, col//3]:
                  return False
                rowSet[row].add(board[row][col]) 
                colSet[col].add(board[row][col]) 
                subGridSet[(row//3, col//3)].add(board[row][col]) 
        return True 