# Input: s = "[{()}]"
# Output: true

def isBalanced(s):
    stk = []
    dct = {')' : '(', ']' : '[', '}' :'{'}
    for ch in s:
        if ch in dct.values():
            stk.append(ch)
        elif ch in dct.keys():
            if not stk:
                return False
                
            if stk[-1] == dct[ch]:
                stk.pop()
            else:
                return False
        
    if not stk:
        return True
    else:
        return False

print(isBalanced(s))
