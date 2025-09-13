# Input:
# s1 = "abcd"
# s2 = "cdab"

# Output: True

def rotation(s1, s2):
  if len(s1) != len(s2):
    return False

  for _ in range(len(s1)):
    if s1 == s2:
      return True
    s1 = s1[-1] + s1[:-1]
  return False

print(rotation(s1, s2))
