class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s = 0,1
        maxProf = 0
        while s < len(prices):
            if(prices[b] < prices[s]):
                maxProf = max(prices[s] - prices[b], maxProf)
            else:
                b=s
            s+=1
        return maxProf