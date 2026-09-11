class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1 # buy, sell
        maximumProfit = 0

        while s < len(prices):
            #Check if profitable
            if (prices[b] < prices[s]):
                sum = prices[s] - prices[b]
                maximumProfit = max(maximumProfit, sum)
            else:
                b = s # We want this to be shifted to the right pointer
            s+=1
        return max(0, maximumProfit)

        # Defined my left and right pointer
        # Defined the maxProfit
        # Defined a loop while my right pointer has not reached end
        # check if value at left pointer less than value at right pointer 
            # calculate the sum difference
            # set maximumprofit to self or item
        # else if right pointer more or equal to left pointer, increment left pointer
        # ALWAYS increment right pointer