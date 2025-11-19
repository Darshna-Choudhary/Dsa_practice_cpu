# Input: txt = "abcab", pattern = "ab"
# Output: [0, 3]

def search(pattern, txt):
    ans = []
    n = len(txt)
    m = len(pattern)
    if m > n:
        return [-1]

    base = 256
    mod = 10**9 + 7
    h = pow(base, m-1, mod)
    pat_h = 0
    win_h = 0
    for i in range(m):
        pat_h = (pat_h * base + (ord(pattern[i]))) % mod
        win_h = (win_h * base + (ord(txt[i]))) % mod
        
    for i in range(n-m+1):
        if pat_h == win_h:
            if txt[i:i+m] == pattern:
                ans.append(i)
            
        if i < n-m:
            win_h = (win_h - (ord(txt[i]) * h)) % mod
            win_h = (win_h * base + ord(txt[i+m])) % mod
            win_h = (win_h + mod) % mod
        
    return ans

print(search(pattern, txt))
