# Input: arr = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
# Output: 2

def rowWithMax1s(arr):
    max_count = float('-inf')
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                count += 1
        if count > max_count:
            max_count = count
            idx = i
    return idx

print(rowWithMax1s(arr))
