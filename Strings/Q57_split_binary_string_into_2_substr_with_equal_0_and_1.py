# Input: str = "0100110101"
# Output: 4

def maxSubStr(str):
	final_count = 0
    z_count = 0
    o_count = 0
    for i in str:
		if i == '0':
			z_count += 1
        else:
            o_count += 1
        if z_count == o_count:
            final_count += 1
    if z_count != o_count:
        return -1
    return final_count

print(maxSubStr(str))
