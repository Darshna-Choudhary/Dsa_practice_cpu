# Input: sum = 12, arr = [5, 1, 3, 4, 7]
# Output: 4
# Explanation: Triplets with sum less than 12 are (1, 3, 4), (5, 1, 3), (1, 3, 7) and (5, 1, 4).

def countTriplets(sum, arr):
    arr.sort()
    n = len(arr)
    count = 0
    for i in range(n-2):
        l = i+1
        r = n-1
        while l < r:
            add = arr[i] + arr[l] + arr[r]
            if add < sum:
                count += r-l
                l += 1
            else:
                r -= 1
    return count

print(countTriplets(sum, arr))
