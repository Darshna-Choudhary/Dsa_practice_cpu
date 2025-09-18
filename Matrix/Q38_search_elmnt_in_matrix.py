# Input:
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3

# Output: True

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = (m * n) -1
    while left <= right:
        mid = left + (right - left) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid-1
    return False

print(searchMatrix(matrix, target))
