# Input: arr = [15, 2, 45, 4 , 7]
# Output: [2, 4]

def valueEqualToIndex(arr):
    ans = []
    for i in range(len(arr)):
        if arr[i] == i+1:
            ans.append(arr[i])
    return ans

print(valueEqualToIndex(arr))
