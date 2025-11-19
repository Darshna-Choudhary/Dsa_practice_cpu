# Input: s = "abab"
# Output: 2

def getLPSLength(s):
    m = len(s)
	lps = [0] * m
	i = 1
	length = 0
	while i < m:
		if s[i] == s[length]:
		    length += 1
		    lps[i] = length
		    i += 1
		else:
		    if length != 0:
		        length = lps[length - 1]
		    else:
		        lps[i] = 0
		        i += 1
	return lps[-1]

print(getLPSLength(s))
