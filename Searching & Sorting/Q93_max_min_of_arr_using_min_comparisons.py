# Question's name and editorial on gfg gives max and min of arr
# but the ques. given to solve is to find middle number from the given three numbers

# Input: a = 978, b = 518, c = 300
# Output: 518

def middle(a, b, c):
    l = [a, b, c]
    l.sort()
    return l[1]
print(middle(a, b, c))
