class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        
        low = prices[0]
        maxp = 0

        for i in prices[1:]:
            if i < low:
                low = i
            else:
                profit = i - low
                if profit > maxp:
                    maxp = profit
        return maxp




        