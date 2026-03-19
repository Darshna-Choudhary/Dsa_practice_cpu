# Input: s = "[{()}]"
# Output: true

def isBalanced(s):
    dct = {"[" : "]", "{" : "}", "(" : ")"}
    stk = []
    for i in s:
        if i in dct.keys():
            stk.append(i)
        else:
            if not stk:
                return False
            if dct[stk[-1]] == i:
                stk.pop()
            else:
                return False
    return not stk

print(isBalanced(s))
