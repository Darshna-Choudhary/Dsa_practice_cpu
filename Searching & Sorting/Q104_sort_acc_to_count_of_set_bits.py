# Input: arr[] = [5, 2, 3, 9, 4, 6, 7, 15, 32]
# Output: [15, 7, 5, 3, 9, 6, 2, 4, 32]

def countbit(x):
    count = 0
    while x:
        x = x & (x-1)
        count += 1
    return count
def sortBySetBitCount(arr):
    arr.sort(key=lambda x:countbit(x), reverse=True)
    return arr

print(sortBySetBitCount(arr))
