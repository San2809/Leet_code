def maxProfit(prices):
    maxprofit = 0
    for i in range(1,len(prices)):
        if(prices[i]>prices[i-1]):
            maxprofit += prices[i]-prices[i-1]

    return maxprofit

print(maxProfit([7,1,5,3,6,4]))