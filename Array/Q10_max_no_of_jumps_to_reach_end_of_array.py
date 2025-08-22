# Input: arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# Output: 3

def minJumps(arr):
	n = len(arr)
	jump = 0
	max_range = 0
	curr_range = 0
	for i in range(n-1):
		max_range = max(max_range, arr[i]+i)
		if i == curr_range:
			if max_range <= i:
				return -1
			else:
				jump += 1
				curr_range = max_range
	return jump

print(minJumps(arr))
