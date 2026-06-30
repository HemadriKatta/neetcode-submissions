class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')
        for price in prices:
            if price < minPrice:
                minPrice = price
            profit = price - minPrice
            if (maxProfit < profit):
                maxProfit = profit
        return maxProfit


                
        