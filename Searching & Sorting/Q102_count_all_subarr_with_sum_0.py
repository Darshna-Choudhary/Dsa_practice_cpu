# Input: arr[] = [0, 0, 5, 5, 0, 0]
# Output: 6

def findSubarray(arr):
    n = len(arr)
    prefix_sum = 0
    count = 0
    dct = {}
    for i in arr:
        prefix_sum += i
        if prefix_sum == 0:
            count += 1
        if prefix_sum in dct:
            count += dct[prefix_sum]
        dct[prefix_sum] = dct.get(prefix_sum, 0) + 1
    return count

print(findSubarray(arr))
