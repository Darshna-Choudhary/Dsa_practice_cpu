# Binary Search Approach

# Input:
# a = [-5, 3, 6, 12, 15]
# b = [-12, -10, -6, -3, 4]

# Output: 0

def medianOf2(a, b):
  n = len(a)
  low, high = 0, n
  while low <= high:
    mid1 = (low + high) // 2
    mid2 = n - mid1

    l1 = float('-inf') if mid1 == 0 else a[mid1-1]
    r1 = float('inf') if mid1 == n else a[mid1]

    l2 = float('-inf') if mid2 == 0 else b[mid2-1]
    r2 = float('inf') if mid2 == n else b[mid2]
    
    if l1 <= r2 and l2 <= r1:
      return (max(l1, l2) + min(r1, r2)) / 2
            
    if l1 > r2:
      high = mid1 - 1
    else:
      low = mid1 + 1
      return 0

print(medianOf2(a,b))
