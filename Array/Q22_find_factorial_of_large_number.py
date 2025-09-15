# Input: n = 10
# Output: [3, 6, 2, 8, 8, 0, 0]

def multiply_list(num, n):
  i = len(num)-1
  carry = 0
  while i >= 0:
    value = num[i] * n + carry
    num[i] = value % 10
    carry = value // 10
    i-= 1
  while carry > 0:
    num.insert(0, carry % 10)
    carry =  carry // 10
  return num
    
def factorial(n):
  ans = [1]
  if n == 1:
    return ans
  for i in range(1, n+1):
    ans = multiply_list(ans, i)
  return ans

print(factorial(n)
