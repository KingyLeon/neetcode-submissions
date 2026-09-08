class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for i, n in enumerate(prices):
            for j, p in enumerate(prices):
                if ( j <= i):
                    continue
                maxProf = max(maxProf, p-n)
        return max(maxProf, 0)