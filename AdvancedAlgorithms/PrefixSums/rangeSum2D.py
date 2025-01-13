"""
input: List[List[int]]
    -> Given a 2D array, you need to be able to get the prefix sum of a sub-square in O(1) time.
"""
class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMatrix = [ [0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMatrix[r][c + 1]
                self.sumMatrix[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        # we need to update the pointers since they reference the original matrix
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomLeft = self.sumMatrix[row2][col2] 
        leftArea = self.sumMatrix[row1 - 1][col2]
        topArea = self.sumMatrix[row2][col1 - 1]
        topLeftCorner = self.sumMatrix[row1 - 1][col1 - 1]

        return bottomLeft - leftArea - topArea + topLeftCorner