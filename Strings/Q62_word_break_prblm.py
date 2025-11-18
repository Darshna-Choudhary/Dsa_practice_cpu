# Input: s = "ilike", dictionary[] = ["i", "like", "gfg"]
# Output: True

def wordBreak(s, dictionary):
    n = len(s)
    word_set = set(dictionary)
    dp = [False] * (n+1)
    dp[0] = True
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]

print(wordBreak(s, dictionary))
