# Input: mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

def spirallyTraverse(mat):
  ans = []
  n = len(mat)
  m = len(mat[0])
  top = 0
  left = 0
  right = m-1
  bottom = n-1
  while top <= bottom and left <= right:
    for i in range(left, right+1):
      ans.append(mat[top][i])
    top += 1
    
    for i in range(top, bottom+1):
      ans.append(mat[i][right])
    right -= 1
            
    if top <= bottom:
      for i in range(right, left-1, -1):
        ans.append(mat[bottom][i])
      bottom -= 1
            
    if left <= right:
      for i in range(bottom, top-1, -1):
        ans.append(mat[i][left])
      left += 1
  return ans

print(spirallyTraverse(mat))
