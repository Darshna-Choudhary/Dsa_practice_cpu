# Input: arr = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, 1]]

def getPairs(arr):
    num_track = ()
    pairs = ()
    for i in arr:
        if -i in num_track:
            pair = tuple(sorted((i, -i)))
            pairs.add(pair)
        num_track.add(i)
    ans = [list(pair) for pair in pairs]
    ans.sort()
    return ans

print(getPairs(arr))
