# Input: s = "ABC"
# Output: ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]

def permutation(s, idx, ans):
    n = len(s)    
    if idx == n:
        ans.append("".join(s))
        return ans
        
    for i in range(idx, n):
        s[i], s[idx] = s[idx], s[i]
        self.permutation(s, idx+1, ans)
        s[i], s[idx] = s[idx], s[i]

def findPermutation(s):
    ans = []
    self.permutation(list(s), 0, ans)
    return list(set(ans))

print(findPermutation(s))
