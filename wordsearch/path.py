def path(grid, ort, i, j):
    grid_len = len(grid)
    orts = {
        "HORIZONTAL": ((i, k, n) for k, n in enumerate(grid[i][j:], j)),
        "VERTICAL": ((k, j, row[j]) for k, row in enumerate(grid[i:], i)),
        "DIAGONAL": (
            (x, y, grid[x][y]) for x, y in zip(range(i, grid_len), range(j, grid_len))
        ),
        "FORWARD DIAGONAL": (
            (x, y, grid[x][y]) for x, y in zip(range(i, -1, -1), range(j, grid_len))
        ),
    }

    for x, y, char in orts.get(ort):
        yield x, y, char
