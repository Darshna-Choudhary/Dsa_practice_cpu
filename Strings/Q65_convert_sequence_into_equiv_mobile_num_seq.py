# Input: S = "GFG"
# Output: 43334

def printSequence(s):
    ans = ""
    l = ["2ABC", "3DEF", "4GHI", "5JKL", "6MNO", "7PQRS", "8TUV", "9WXYZ"]
    for i in range(len(s)):
        if s[i] == " ":
            ans += "0"
        for j in l:
            if s[i] in j:
                ans += j[0]*(j.find(s[i]))
                break
    return ans

print(printSequence(s))
