def get_partial_diagonal(li, dim, x, y, indices=False):
    # this is disgusting, but will be refactored eventually.
    # this is a quick way to correctly place words via forward diagonals.

    i = x
    j = y
    result = []
    while i >= 0 and j < dim:
        if indices is True:
            result.append((i, j))
        else:
            result.append(li[i][j])
        i -= 1
        j += 1

    return result
