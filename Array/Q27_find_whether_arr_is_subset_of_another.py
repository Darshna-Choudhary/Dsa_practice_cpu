# Input:
# a = [11, 7, 1, 13, 21, 3, 7, 3]
# b = [11, 3, 7, 1, 7]

# Output: True

def isSubset(a, b):
  a.sort()
  b.sort()
  j = 0
  for i in range(len(a)):
    if a[i] == b[j]:
      j += 1
    if j == len(b):
      return True
  return False

print(isSubset(a,b))
