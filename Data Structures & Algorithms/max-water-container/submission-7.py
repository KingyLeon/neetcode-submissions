class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1

        result = 0
        maxHeight = 0
        # Area = Height x Width
        # Area = min(heights(L),heights(R)) x abs(L-R)
        maxDigits = [0, 0]
        while L < R:
            h = min(heights[L], heights[R])
            Area = h * abs(R-L)
            result = max(result, Area)
            if (heights[L] < heights[R]):
                L += 1
            else:
                R -= 1
        return result