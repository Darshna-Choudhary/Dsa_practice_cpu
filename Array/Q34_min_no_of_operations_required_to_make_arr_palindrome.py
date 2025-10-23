# Input: arr = [111, 222, 333, 444, 555]
# Output: True

def checkPalindrome(num):
  s_num = str(num)
  if s_num == s_num[::-1]:
    return True
  else:
    return False
    
def isPalinArray(arr):
  return all(checkPalindrome(n) for n in arr)

print(isPalinArray(arr))
