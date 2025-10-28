# Input: mat = [[1 2 3], [4 5 6], [7 8 9]]
# Output:   7 4 1 
#           8 5 2
#           9 6 3

def rotate(mat): 
    for i in range(n // 2):
        for j in range(i, n-i-1):
            temp = mat[i][j]
            mat[i][j] = mat[n-j-1][i]
            mat[n-j-1][i] = mat[n-i-1][n-j-1]
            mat[n-i-1][n-j-1] = mat[j][n-i-1]
            mat[j][n-i-1] = temp
    return mat

print(rotate(mat))
