# Input: arr = [2, 4, 1, 7, 5, 0]
# Output: [2, 4, 5, 0, 1, 7]

def rev(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def nextPermutation(arr):
    n = len(arr)
    k, l = -1, -1
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            k = i
            break
        
    for i in range(k+1, n):
        if arr[k] < arr[i]:
            l = i

    if k == -1:
        arr.reverse()
    else:
        arr[k], arr[l] = arr[l], arr[k]
        rev(arr, k+1, n-1)
    return arr

print(nextPermutation(arr))
