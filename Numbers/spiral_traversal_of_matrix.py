def snail(mat):
    m, n = len(mat), len(mat[0])
    res = []
    # Define the boundaries of the matrix
    top, bottom, left, right = 0, m - 1, 0, n - 1

    # Iterate until the boundaries overlap then switch the direction
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            res.append(mat[top][i])
        top += 1
        for i in range(top, bottom + 1):
            res.append(mat[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(mat[i][left])
            left += 1
    return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(snail(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]