# Input: mat = [[1, 2, 1, 4, 8], [3, 7, 8, 5, 1], [8, 7, 7, 3, 1], [8, 1, 2, 7, 9]]
# Output = 1,8 or 8,1

def findcommon(mat):
    ans = []
    m = len(mat)
    n = len(mat[0])
    for j in range(n):
        elmnt = mat[0][j]
        present = True
        if elmnt in ans:
            continue

        for i in range(1, m):
            found = False
            for k in range(n):
                if mat[i][k] == elmnt:
                    found = True
                    break
            if not found:
                present = False
                break

        if present:
            ans.append(elmnt)
    return ans

print(findcommon(mat))
