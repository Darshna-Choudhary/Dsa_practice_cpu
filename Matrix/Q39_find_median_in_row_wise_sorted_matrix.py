# Input:
# mat[][] = [[1, 3, 5], 
#            [2, 6, 9],
#            [3, 6, 9]]

# Output: 5

def median(mat):
  ans = []
  for i in mat:
    for j in i:
      ans.append(j)

  ans.sort()
  return ans[len(ans) // 2]

print(median(mat))
