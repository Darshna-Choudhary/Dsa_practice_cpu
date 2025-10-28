# Input: mat = [[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]]
#        k = 3
# Output: 27

import heapq
def kthSmallest(mat, k):
    n = len(mat)
    minheap = []
    visited = set()
    heapq.heappush(minheap, (mat[0][0], 0, 0))
    visited.add((0, 0))

    for _ in range(k):
        val, i, j = heapq.heappop(minheap)
        if i+1 < n and (i+1, j) not in visited:
            heapq.heappush(minheap, (mat[i+1][j], i+1, j))
            visited.add((i+1, j))
    
        if j+1 < n and (i, j+1) not in visited:
            heapq.heappush(minheap, (mat[i][j+1], i, j+1))
            visited.add((i, j+1))
    return val

print(kthSmallest(mat, k))
