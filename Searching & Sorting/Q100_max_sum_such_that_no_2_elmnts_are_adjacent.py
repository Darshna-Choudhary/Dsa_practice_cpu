# Input: arr = [5, 3, 4, 11, 2]
# Output: 16

def findMaxSum(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr)

    dp = [-1] * (n)
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    temp = 0
        
    for i in range(2, n):
        temp = arr[i] + dp[i-2]
        dp[i] = max(dp[i-1], temp)
    return dp[-1]

print(findMaxSum(arr))
