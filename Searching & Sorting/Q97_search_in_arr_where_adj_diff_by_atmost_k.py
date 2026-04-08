Input: arr = [4, 5, 6, 7, 6] , k = 1 , x = 6
Output: 2

def findStepKeyIndex(arr, k, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

print(findStepKeyIndex(arr, k, x))
