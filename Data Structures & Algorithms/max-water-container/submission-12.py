class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1

        maxArea = 0
        while L < R:
            width = abs(R - L)
            h = min(heights[L], heights[R])
            area = h * width
            maxArea = max(area, maxArea)
            if (heights[L] < heights[R]):
                L += 1
            else: # Runs when equal and heights[R] < heights[L] no need for explicit case
                R -= 1
        return maxArea
            