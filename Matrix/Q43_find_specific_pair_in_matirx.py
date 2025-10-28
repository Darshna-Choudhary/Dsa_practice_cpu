# Input: mat = [[ 1, 2, -1, -4, -20 ], [ -8, -3, 4, 2, 1 ], [ 3, 8, 6, 1, 3 ], [ -4, -1, 1, 7, -6 ], [ 0, -4, 10, -5, 1 ]]
# Output: 18

def findMaxValue(n, mat):
    maxv = float('-inf')
    maxArr = [[0 for j in range(n)] for i in range(n)]
    maxArr[n-1][n-1] = mat[n-1][n-1]

    maxv = mat[n-1][n-1]
    for j in range(n-2, -1, -1):
        if mat[n-1][j] > maxv:
            maxv = mat[n-1][j]
        maxArr[n-1][j] = maxv

    maxv = mat[n-1][n-1]
    for i in range(n-2, -1, -1):
        if mat[i][n-1] > maxv:
            maxv = mat[i][n-1]
        maxArr[i][n-1] = maxv

    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            if maxArr[i+1][j+1] - mat[i][j] > maxv:
                maxv = maxArr[i+1][j+1] - mat[i][j]
            maxArr[i][j] = max(mat[i][j], max(maxArr[i+1][j], maxArr[i][j+1]))
    return maxv

print(findMaxValue(5, mat))
