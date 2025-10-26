# Binary Search Approch

# Input:
# a = [3, 5, 6, 12, 15]
# b = [3, 4, 6, 10, 10, 12]

# Output: 6

def medianOf2(a, b):
  n = len(a)
  m = len(b)
  if n > m:
    return medianOf2(b, a)
  low = 0
  high = n
  while low <= high:
    mid1 = (low + high) // 2
    mid2 = ((n + m + 1) // 2) - mid1
            
    l1 = float('-inf') if mid1 == 0 else a[mid1 - 1]
    r1 = float('inf') if mid1 == n else a[mid1]

    l2 = float('-inf') if mid2 == 0 else b[mid2 - 1]
    r2 = float('inf') if mid2 == m else b[mid2]

    if l1 <= r2 and l2 <= r1:
      if (n + m) % 2 == 0:
        return (max(l1, l2) + min(r1, r2)) / 2.0
      else:
        return max(l1, l2)
            
    if l1 > r2:
      high = mid1 - 1
    else:
      low = mid1 + 1
  return 0

print(medianOf2(a, b))
