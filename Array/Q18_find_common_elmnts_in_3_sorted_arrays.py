# Input:
# arr1 = [1, 5, 10, 20, 40, 80]
# arr2 = [6, 7, 20, 80, 100]
# arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Output: [20, 80]

def commonElements(arr1, arr2, arr3):
    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)
    b = s3.intersection(s1.intersection(s2))
    if len(b) >= 1:
        return list(sorted(b))
    else:
        return [-1]

print(commonElements(arr1, arr2, arr3))
