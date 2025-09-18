# Input:
# arr = [1, 4, 45, 6, 0, 19]
# x = 51

# Ouput: 2

def smallestSubWithSum(arr, x):
  ans = float('inf')
  left = 0
  sum = 0
  for i in range(len(arr)):
    sum += arr[i]
    while sum >= x:
      ans = min(ans, i-left+1)
      sum -= arr[left]
      left += 1
  return ans if ans != float('inf') else 0

print(smallestSubWithSum(arr, x))
