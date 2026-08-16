class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        l, r = 0, len(heights) - 1

        while l < r:
            h1 = heights[l]
            h2 = heights[r]
            d = r - l

            h = min(h1, h2)
            maxArea = max(maxArea, d * h)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1

        return maxArea