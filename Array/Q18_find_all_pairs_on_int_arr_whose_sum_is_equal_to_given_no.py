# Input: arr = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, 1]]

def getPairs(arr):
    dct = {}
    pairs = set()
    for i in arr:
        dct[i] = dct.get(i, 0)+1
        
    for i in arr:
        if -i in dct:
            if i == 0 and dct[i] < 2:
                continue
            pair = tuple(sorted((i, -i)))
            pairs.add(pair)
    ans = sorted([list(p) for p in pairs])
    return ans

print(getPairs(arr))
