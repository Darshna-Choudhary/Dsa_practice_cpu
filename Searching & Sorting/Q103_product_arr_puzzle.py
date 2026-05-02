# Input: arr[] = [10, 3, 5, 6, 2]
# Output: [180, 600, 360, 300, 900]

def productExceptSelf(arr):
    n = len(arr)
    ans = [1] * (n)
    for i in range(1, n):
        ans[i] = ans[i-1] * arr[i-1]
        
    right = 1
    for i in range(n-1, -1, -1):
        ans[i] = ans[i] * right
        right *= arr[i]
    return ans

print(productExceptSelf(arr))
