# Input:
# arr = [3, 4, 2, 2, 1, 2, 3, 3]
# k = 4

# Output: 2
from collections import Counter
def find_freq(arr, k):
  n = len(arr)
  dct = Counter(arr)
  count = 0
  for key, v in dct.items():
    if v > (n // k):
      count += 1
  return count

print(find_freq(arr, k))
