# Input:
# first = "XY"
# second = "12"
# results = ["1XY2", "Y1X2", "Y21XX"]

# Output: Valid shuffle

def checklen(first, sec, res):
    if len(first) + len(sec) == len(res):
        return True
    else:
        return False

def sortStr(s):
    arr = []
    for i in s:
        arr.append(i)
    arr.sort()
    s = ''.join(arr)
    return arr

def shuffle(first, sec, res):
    first = sortStr(first)
    sec = sortStr(sec)
    res = sortStr(res)
    i = j = k = 0
    while k < len(res):
        if i < len(first) and first[i] == res[k]:
            i += 1
        elif j < len(sec) and sec[j] == res[k]:
            j += 1
        else:
            return False
        k += 1
    return True

def checkShuffle(first, second, results):
    for res in results:
        if checklen(first, second, res) == True and shuffle(first, second, res) == True:
            return "Valid shuffle"
        else:
            return "Invalid shuffle"

print(checkShuffle(first, second, results))
