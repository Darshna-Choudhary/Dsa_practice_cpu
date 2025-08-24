# Input: arr = [12, 31, 35, 8, 32, 17]
# Output: 7

def mergeSort(arr, st, end):
    incount = 0
    if st < end:
        mid = st + (end - st) // 2
        incount += mergeSort(arr, st, mid)
        incount += mergeSort(arr, mid+1, end)
        incount += merge(arr, st, mid, end)
    return incount

def merge(arr, st, mid, end):
    invcount = 0
    i = st
    j = mid+1
    temp = []
        
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            invcount += (mid - i + 1)
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= end:
        temp.append(arr[j])
        j += 1
        
    for idx in range(0, len(temp)):
        arr[idx+st] = temp[idx]
    return invcount
    
def inversionCount(arr):
    return mergeSort(arr, 0, len(arr)-1)

print(inversionCount(arr))    
