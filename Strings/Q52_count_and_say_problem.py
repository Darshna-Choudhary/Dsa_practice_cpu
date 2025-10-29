# Input: n = 4
# Output: "1211"

def encode(s):
    freq = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            freq.append([s[i-1], count])
            count = 1
    freq.append([s[-1], count])
    return freq
    
def decode(dct):
    s = ""
    for ch, cnt in dct:
        s += str(cnt) + ch
    return s

def countAndSay(n):
    if n == 1:
        return str(n)
    ans = "1"
    for i in range(1, n):
        f = encode(ans)
        ans = decode(f)
    return ans

print(countAndSay(4))
