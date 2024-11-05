# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

def matrixDFS(grid, r, c, visit):
    ROWS, COLUMNS = len(grid), len(grid[0])
    if (min(r,c) < 0 or r == ROWS or c == COLUMNS or ((r,c) in visit) or grid[r][c] == 1):
        return 0
    if (r == ROWS-1 and c == COLUMNS-1):
        return 1
    
    # if we haven't reached any of the base cases, we need to add the recently visited point to the hash set 
    visit.add((r,c))
    # before the recursion starts, count is initialized
    count = 0
    # now all the possible movements are recursively explored
    count += matrixDFS(grid, r + 1, c, visit)
    count += matrixDFS(grid, r - 1, c, visit)
    count += matrixDFS(grid, r , c + 1, visit)
    count += matrixDFS(grid, r , c - 1, visit)

    # finally if we explored successfully or unsuccessfully the points on a grid
    visit.remove((r,c))
    return count

print(matrixDFS(grid, 0, 0, set()))