# Input: arr = [3, 2, 2, 5], k = 6
# Output: 10

def solveWordWrap(arr, k):
    n = len(arr)
    dp = [0] * n
    ans = [0] * n
    dp[n-1] = 0
    ans[n-1] = n-1
    for i in range(n-2, -1, -1):
        currlen = -1
        dp[i] = float('inf')
        for j in range(i, n):
            currlen += arr[j] + 1
            if currlen > k:
                break
            if j == n-1:
                cost = 0
            else:
                extra_space = (k-currlen) ** 2
                cost = extra_space + dp[j+1]
            if cost < dp[i]:
                dp[i] = cost
                ans[i] = j
    i, res = 0, 0
    while i < n:
        pos = 0
        for j in range(i, ans[i] + 1):
            pos += arr[j]
            x = ans[i] - i
            if ans[i] + 1 != n:
                res += (k - x - pos) ** 2
        i = ans[i] + 1
    return res

print(solveWordWrap(arr, k))
