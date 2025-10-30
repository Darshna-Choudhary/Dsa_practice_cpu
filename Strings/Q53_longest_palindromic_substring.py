# Input: s = “forgeeksskeegfor” 
# Output: “geeksskeeg”
def longestPalindrome(s):
    start = 0
    end = 0
    for i in range(len(s)):
        low = i-1
        high = i
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > end:
                end = high - low + 1
                start = low
            low -= 1
            high += 1
            
        low = i-1
        high = i+1
        while low >= 0 and high < len(s) and s[low] == s[high]:
            if high - low + 1 > end:
                end = high - low + 1
                start = low
            low -= 1
            high += 1
    if end == 0:
        return s[start]
    return s[start:start+end]

print(longestPalindrome(s))
