# Input: s = "abc"
# Output: [[], ['c'], ['b'], ['b', 'c'], ['a'], ['a', 'c'], ['a', 'b'], ['a', 'b', 'c']]

def getPermute(s):
    n = len(s)
    ans = []
    for i in range(2 ** n):
        bn = bin(i)[2:]

        if (n-len(bn)) >= 0:
            bn = '0' * (n-len(bn)) + bn
            temp = []
            for k in range(n):
                if bn[k] == '1':
                    temp.append(s[k])
            ans.append(temp)
    return ans

print(getPermute(s))
