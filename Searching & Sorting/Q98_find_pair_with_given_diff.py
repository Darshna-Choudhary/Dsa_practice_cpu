# Input: arr = [5, 20, 3, 2, 5, 80], x = 78
# Output: true

def findPair(arr):
    n = len(arr)
    arr.sort()
    i, j = 0, 1
    while (j < n) and (i < n):
        diff = arr[j] - arr[i]
        if diff == x and i != j:
            return True
        elif diff < x:
            j += 1
        else:
            i += 1
    return False

print(findPair(arr))
