# Input: n = 4
# Output: "1211"

def countAndSay(n):
    if n == 1:
        return str(n)

    ans = "1"
    for _ in range(n-1):
        curr = ""
        count = 1
        for i in range(1, len(ans)):
            if ans[i] == ans[i-1]:
                count += 1
            else:
                curr += str(count) + str(ans[i-1])
                count = 1
        curr += str(count) + str(ans[-1])
        ans = curr
    return ans

print(countAndSay(n))
