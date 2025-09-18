# Input:
# arr = [3, 4, 1, 9, 56, 7, 9, 12]
# m = 5

# Output: 6

def findMinDiff(arr, m):
  n = len(arr)
  arr.sort()
  diff = float('inf')
  for i in range(n):
    if i+m-1 < n:
      diff = min(diff, arr[i+m-1] - arr[i])
  return diff

print(findMinDiff(arr, m))
