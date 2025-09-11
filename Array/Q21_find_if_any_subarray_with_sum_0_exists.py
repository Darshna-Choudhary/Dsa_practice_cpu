# Input: arr = [4, 2, -3, 1, 6]
# Output: True

def subArrayExists(arr):
  curr_sum = 0
  sums = set()
  for i in arr:
    curr_sum += i
    if i == 0 or curr_sum == 0 or curr_sum in sums:
      return True
    sums.add(curr_sum)
  return False

print(subArrayExists(arr))
