# Input: arr = [10, 2, 3, 4, 5, 7, 8], target = 23
# Output: [[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]]

def fourSum(arr, target):
    n = len(arr)
    arr.sort()
    ans = set()
    for i in range(n):
        for j in range(i+1, n):
            visited = set()
            for k in range(j+1, n):
                num4 = target - (arr[i] + arr[j] + arr[k])
                if num4 in visited:
                    temp = tuple(sorted((arr[i], arr[j], arr[k], num4)))
                    ans.add(temp)
                visited.add(arr[k])
    return list(ans)

print(fourSum(arr, target))
