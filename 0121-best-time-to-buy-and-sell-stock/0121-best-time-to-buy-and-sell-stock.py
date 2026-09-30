class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0 

        buyPrice  = float('inf')
        for price in prices:
            if price < buyPrice:
                buyPrice = price
            currProfit = price - buyPrice
            maxProfit = max(maxProfit,currProfit)
        return maxProfit
    