class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = prices[2] - prices[1]
        b, s = 0, 1
        maximumProfit = 0

        while s < len(prices):
            #Check if proftiable
            if (prices[b] < prices[s]):
                sum = prices[s] - prices[b]
                maximumProfit = max(maximumProfit, sum)
            else:
                b = s # We want this to be shifted to the right pointer
            s+=1
        return max(0, maximumProfit)