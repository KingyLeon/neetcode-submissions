class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        maxProfit = 0

        while s < len(prices):
            if(prices[b] < prices[s]):
                sum = prices[s] - prices[b]
                maxProfit = max(sum, maxProfit)
            else:
                b = s
            s += 1
        
        return max(maxProfit, 0)