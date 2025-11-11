# Input: s1 = "geek", s2 = "gesek"
# Output: 1

def editDistance(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    # base case
    # if s2 is empty
    for i in range(n+1):
        dp[i][0] = i

    # if s1 is empty
    for j in range(m+1):
		dp[0][j] = j
		
    for i in range(1, n+1):
		for j in range(1, m+1):
		    if s1[i-1] == s2[j-1]:
		        dp[i][j] = dp[i-1][j-1]
		    else:
		        insert = 1 + dp[i][j-1]
		        delete = 1 + dp[i-1][j]
		        replace = 1 + dp[i-1][j-1]
		        dp[i][j] = min(insert, min(delete, replace))
    return dp[n][m]

print(editDistance(s1, s2))
