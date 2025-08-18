# Input: arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# Output: [-12, -13, -5, -7, -3, -6, 5, 6, 11]

def seprt_arr(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
    return arr

print(seprt_arr(arr))
