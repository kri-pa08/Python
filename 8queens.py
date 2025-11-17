def isSafe(mat, row, col):
    n = len(mat)

    # Check vertical
    for i in range(row):
        if mat[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if mat[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if mat[i][j]:
            return False
        i -= 1
        j += 1

    return True


def placeQueens(row, mat):
    n = len(mat)

    if row == n:
        return True

    for col in range(n):
        if isSafe(mat, row, col):
            mat[row][col] = 1

            if placeQueens(row + 1, mat):
                return True

            mat[row][col] = 0  # Backtrack

    return False


def queens():
    n = 8
    mat = [[0] * n for _ in range(n)]
    placeQueens(0, mat)
    return mat


if __name__ == "__main__":
    res = queens()
    for row in res:
        print(" ".join(map(str, row)))
