# Input: arr = [-2, 6, -3, -10, 0, 2]
# Output: 180

def maxProduct(arr):
  max1 = arr[0]
  min1 = arr[0]
  max_prod = arr[0]
  for i in range(1, len(arr)):
    n = arr[i]
    if n < 0:
      max1, min1 = min1, max1
    max1 = max(n, n * max1)
    min1 = min(n, n * min1)
    max_prod = max(max_prod, max1)
  return max_prod

print(maxProduct(arr))
