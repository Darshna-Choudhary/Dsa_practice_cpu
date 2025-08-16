# Input :
# arr =  [7, 10, 4, 3, 20, 15]
# k = 3

# Output :
# kth minimum of array: 7
# kth maximum of array: 10

def kthSmallest(arr,k):
    for i in range(k-1):
        arr.remove(max(arr))
        arr.remove(min(arr))
    min_elmnt = min(arr)
    max_elmnt = max(arr)

    print("kth minimum of array:",min_elmnt)
    print("kth maximum of array:",max_elmnt)

print(kthSmallest(arr, k))
