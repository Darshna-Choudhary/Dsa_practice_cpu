# Input:
# arr = [1, 5, 8, 10]
# k = 2

# Output: 5

def getMinDiff(self, arr, k):
        arr = sorted(arr)
        n = len(arr)
        
        if n == 1:
            return 0

        ans = arr[-1] - arr[0]
        small = arr[0]+k
        large = arr[n-1]-k

        for i in range(len(arr)-1):
            minh = min(small, arr[i+1]-k)
            maxh = max(large, arr[i]+k)
            
            if minh < 0:
                continue
            ans = min(ans, maxh - minh)
        return ans
  print(getMinDiff(arr, k))
