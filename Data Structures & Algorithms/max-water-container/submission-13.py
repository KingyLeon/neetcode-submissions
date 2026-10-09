class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        maxArea = 0

        while L < R:
            subTotal = abs(R-L) * min(heights[R], heights[L])
            maxArea = max(subTotal, maxArea)
            if (heights[R] < heights[L]):
                R -= 1
            else:
                L +=1
        return maxArea