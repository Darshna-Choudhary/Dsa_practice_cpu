# Input: arr = [2, 6, 1, 9, 4, 5, 3]
# Output: 6

def longestConsecutive(arr):
  arr=sorted(set(arr))
  count=1
  ms=1
  for i in range(1,len(arr)):
    if arr[i]==arr[i-1]+1:
      count+=1
      ms=max(ms,count)
    else:
      count=1
  return ms

print(longestConsecutive(arr))
