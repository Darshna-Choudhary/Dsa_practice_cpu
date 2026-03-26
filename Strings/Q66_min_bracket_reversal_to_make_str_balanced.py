# Input: s = "}{{}}{{{"
# Output: 3

def countminreversals(s):
    n = len(s)
    if n%2 != 0:
        return -1
    stk = []
    for i in range(n):
        if s[i] == "{":
            stk.append(s[i])
        else:
            if stk and stk[-1] == "{":
                stk.pop()
            else:
                stk.append(s[i])
    op, cl = 0, 0
    while stk:
        if stk[-1] == "{":
            op += 1
        else:
            cl += 1
        stk.pop()
    return ((op+1)//2) + ((cl+1)//2)

print(countminreversals(s))
