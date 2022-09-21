def maxProfit(prices: list[int]):
    n = len(prices)
    profit = 0
    for i in range(len(prices)):
        price = prices[i]
        if price < prices[i+1]:
            profit += prices[i+1] - price
    
    return profit

maxProfit([7,1,5,3,6,4])
