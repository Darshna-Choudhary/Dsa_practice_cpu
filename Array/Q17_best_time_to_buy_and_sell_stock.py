# Input: prices = [7,1,5,3,6,4]
# Output: 5

def maxProfit(prices):
    bestBuy = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > bestBuy:
            max_profit = max(max_profit, prices[i]-bestBuy)
        bestBuy = min(bestBuy, prices[i])
    return max_profit

print(maxProfit(prices))
