# Input: mat[][] = [[0, 1, 1, 0],
#                   [1, 1, 1, 1],
#                   [1, 1, 1, 1],
#                   [1, 1, 0, 0]]
# Output: 8

def rect(a):
    a = a + [0]
    max_area = a[0]
    s = []
    i = 0
    n = len(a)
    while i < n:
        if (not s) or (a[i] > a[s[-1]]):
            s.append(i)
            i += 1
        else:
            top = s.pop()
            height = a[top]
            width = i if (not s) else (i-s[-1]-1)
            max_area = max(max_area, height * width)
    return max_area
        
def maxArea(mat):
    col = len(mat[0])
    max_area = float('-inf')
    h = [0] * col
    for i in range(len(mat)):
        for j in range(col):
            h[j] = h[j] + 1 if mat[i][j] == 1 else 0
        max_area = max(max_area, self.rect(h))
    return max_area

print(maxArea(mat))
