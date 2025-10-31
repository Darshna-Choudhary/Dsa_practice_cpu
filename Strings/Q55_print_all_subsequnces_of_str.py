# Input: s = "abc"
# Output: [[], ['c'], ['b'], ['b', 'c'], ['a'], ['a', 'c'], ['a', 'b'], ['a', 'b', 'c']]

def getSubSeq(s, i):
    j = 0
    sub = ""
    while i > 0:
        if i & 1:
          sub += s[j]
        j += 1
        i = i >> 1
    return sub

def createSub(s):
    ans = []
    for i in range(1, (1 << len(s))):
        ans.append(getSubSeq(s, i))
    return ans

print(createSub(s))
