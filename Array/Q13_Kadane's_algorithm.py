# Input: arr = [2, 3, -8, 7, -1, 2, 3]
# Output: 11

def maxSubarraySum(arr):
        sum = 0
        max_sum = float('-inf')
        for i in arr:
            sum += i
            max_sum = max(sum, max_sum)
            if sum < 0:
                sum = 0
        return max_sum
  
print(maxSubarraySum(arr))
