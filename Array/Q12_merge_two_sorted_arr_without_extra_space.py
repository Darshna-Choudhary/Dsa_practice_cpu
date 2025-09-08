# Bubble sort
# Input: arr = [2, 3, 1, 5, 4]
# Output: [1, 2, 3, 4, 5]

def merge_arr(arr):
  for i in range(len(arr)-1, -1, -1):
    for j in range(i-1, -1, -1):
      if arr[i] < arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
  return arr

print(merge_arr(arr))
