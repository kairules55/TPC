
directions = [(0,1), (1,0), (-1, 0), (0,-1)]


def dfs(r, c, grid):
    if not 0 <= r < len(grid) and not 0 <= c < len(grid[0]) and grid[r][c] != 1:
        return 0
    
    size = 0
    for r_inc, c_inc in directions:
        r_new = r + r_inc
        c_new = c + c_inc
        if 0 <= r_new < len(grid) and 0 <= c_new < len(grid[0]) and grid[r_new][c_new] == 1:
            grid[r_new][c_new] = -1
            size += 1 + dfs(r_new, c_new, grid)

    return size


def no_of_islands(grid):
    rows = len(grid)
    cols = len(grid[0])

    max_island = 0
    num_island = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                num_island += 1
                max_island = max(max_island, dfs(row, col, grid))

    return (num_island, max_island)

grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]

print(no_of_islands(grid))

        
