# Input: arr = [1, 4, 3, 2, 6, 5]
# Output: [5, 6, 2, 3, 4, 1]

def reverse_arr(arr):
    n = len(arr)
    
    for i in range(n // 2):
        a = arr[i]
        arr[i] = arr[n-1]
        arr[n-1] = a
        n -= 1
    return arr

print(reverse_arr(arr))
