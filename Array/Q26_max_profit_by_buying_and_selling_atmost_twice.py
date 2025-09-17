# Input: prices = [10, 22, 5, 75, 65, 80]
# Output: 87

def maxProfit(prices):
  n = len(prices)
  profit = [0] * n
  maxprice = prices[-1]
  for i in range(n-2, -1, -1):
    maxprice = max(maxprice, prices[i])
    profit[i] = max(profit[i+1], maxprice - prices[i])
  
  ans = 0
  minprice = prices[0]
  for i in range(1, n):
    minprice = min(minprice, prices[i])
    ans = max(ans, profit[i] + (prices[i] - minprice))
  return ans

print(maxProfit(prices))
