# Input:
# arr = [2, 1, 5, 6, 3]
# k = 3

# Output: 1

def minSwap (arr, k) :
  n = len(arr)
  count = sum(1 for x in arr if x <= k)        
  if count == 0 or count == n:
    return 0
    
  bad =  sum(1 for i in range(count) if arr[i] > k)
  ans = bad
        
  for i in range(n - count):
    if arr[i] > k:
      bad -= 1
    if arr[i + count] > k:
      bad += 1
    ans = min(ans, bad)
  return ans

print(minSwap(arr, k))
