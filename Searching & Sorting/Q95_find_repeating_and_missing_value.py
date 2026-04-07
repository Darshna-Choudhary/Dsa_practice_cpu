# Input: arr = [2, 2]
# Output: [2, 1]

def findTwoElement(arr):
    n = len(arr)
    actual = n*(n+1) // 2
    arr_sum = sum(arr)
        
    actual_sq = n*(n+1)*(2*n+1)//6
    arr_sum_sq = sum(x*x for x in arr)
        
    s = actual - arr_sum
    p = actual_sq - arr_sum_sq
        
    r_plus_m = p // s
    r = (s + r_plus_m) // 2
    m = r - s
    return [m, r]

print(findTwoElement(arr))
