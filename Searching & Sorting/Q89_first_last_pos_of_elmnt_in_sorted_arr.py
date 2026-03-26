# Input: arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
# Output: [2, 5]

def find(arr, x):
    n = len(arr)
    ans = [-1, -1]
    start, end = 0, n-1
    while start <= end:
        mid = start + (end-start) // 2
        if arr[mid] == x:
            ans[0] = mid
            end = mid - 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
        
    start, end = 0, n-1
    while start <= end:
        mid = start + (end-start) // 2
        if arr[mid] == x:
            ans[1] = mid
            start = mid + 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return ans

print(find(arr, x))
