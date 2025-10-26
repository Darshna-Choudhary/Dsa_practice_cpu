# Input:
# N=4
# mat=[[10,20,30,40],
# [15,25,35,45] 
# [27,29,37,48] 
# [32,33,39,50]]

# Output:
# 10 15 20 25 
# 27 29 30 32
# 33 35 37 39
# 40 45 48 50

def sortedMatrix(N, mat):
    ans = []
    for i in mat:
        for j in i:
            ans.append(j)
    ans.sort()
    k = 0
    for i in range(N):
        for j in range(N):
            mat[i][j] = ans[k]
            k += 1
    return mat

print(sortedMatrix(N, mat))
