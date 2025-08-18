# Input: arr = [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]

def rotate(arr):
    i, j = 0, len(arr)-1
    while i != j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr
  
print(rotate(arr))
