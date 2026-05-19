# Input: arr[] = [2, 8, 5, 4]
# Output: 1

def minSwaps(arr):
    swap = 0
	n = len(arr)
	pos = {v:i for i, v in enumerate(arr)}
	sorted_arr = sorted(arr)
	    
	for i in range(n):
	    if arr[i] != sorted_arr[i]:
	        swap += 1
	        correct_val = sorted_arr[i]
	        correct_pos = pos[correct_val]
	        arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
	        pos[arr[correct_pos]] = correct_pos
	        pos[arr[i]] = i
	return swap

print(minSwaps(arr))
