# Input: arr = [1, 4, 45, 6, 10, 8]
# Output: target = 13

def hasTripletSum(arr, target):
  n = len(arr)
  arr.sort()
  for i in range(n-2):
    l = i+1
    r = n-1
    while l < r:
      total = arr[i] + arr[l] + arr[r]
      if total == target:
        return True
      elif total < target:
        l += 1
      else: r -= 1
  return False

print(hasTripletSum(arr, target))
