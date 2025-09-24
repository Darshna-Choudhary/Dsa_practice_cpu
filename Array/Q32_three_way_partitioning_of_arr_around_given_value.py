# Input: arr = [1, 2, 3, 3, 4], a = 1, b = 2
# Outpt: True

def threeWayPartition(arr, a, b):
    i, j, k = 0, len(arr)-1, 0
    while k <= j:
        if arr[k] < a:
            arr[k], arr[i] = arr[i], arr[k]
	        i += 1
	        if i > k:
                k += 1
	    elif arr[k] > b:
            arr[k], arr[j] = arr[j], arr[k]
	        j -= 1
	    else:
	        k += 1

print(threeWayPartition(arr, a, b))
