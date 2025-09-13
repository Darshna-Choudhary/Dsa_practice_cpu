# Input: s = "geeksforgeeks"
# Output: ['e', 4], ['g', 2], ['k', 2], ['s', 2]

from collections import Counter
def count_freq(s):
  dct = Counter(s)
  ans = []
  for k, v in dct.items():
    if v > 1:
      ans.append([k,v])
  ans.sort(key = lambda x:x[1], reverse = True)
  return ans

print(count_freq(s))
