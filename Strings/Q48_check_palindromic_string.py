# Input: s = "abba"
# Output: True

def isPalindrome(s):
  if s[0] != s[-1]:
    return False
            
  i = 0
  j = len(s)-1
  while i <= j:
    if s[i] != s[j]:
      return False
    i += 1
    j -= 1
  return True

print(isPalindrome(s))
