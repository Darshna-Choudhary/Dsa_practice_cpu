# Input: s = ["h","e","l","l","o"]
# Output: ['o', 'l', 'l', 'e', 'h']

def reverseString(s):
  j = len(s)-1
  for i in range(len(s)//2):
    s[i], s[j] = s[j], s[i]
    j -= 1
  return s

print(reverseString(s))
