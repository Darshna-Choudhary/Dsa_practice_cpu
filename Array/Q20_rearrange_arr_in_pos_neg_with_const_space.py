# Input: arr = [1, 2, 3, -4, -1, 4]
# Output: [1, -4, 2, -1, 3, 4]

def rotate(arr, st, end):
  temp = arr[j]
  for i in range(end, st, -1):
    arr[i] = arr[i-1]
  arr[i] = temp
  return arr

def arrange(arr):
  n = len(arr)
  for i in range(n):
    if arr[i] >= 0 and i % 2 == 1:
      for j in range(i+1, n):
        if arr[j] < 0:
          rotate(arr, i, j)
          break

    elif arr[i] < 0 and i % 2 == 0:
      for j in range(i+1, n):
        if arr[j] >= 0:
          rotate(arr, i, j)
          break
  return arr

print(arrange(arr))
