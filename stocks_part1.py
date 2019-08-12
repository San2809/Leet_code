def maxProfit(prices):
    minprices = 2147483647
    maxprofit = 0

    for i in range(len(prices)):

        if(prices[i]<minprices):
            minprices = prices[i]

        elif(prices[i]-minprices>maxprofit):
            maxprofit = prices[i]-minprices
    return maxprofit

print(maxProfit([7,1,5,3,6,4]))