class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer
        l = 0
        r = len(heights) - 1
        maxarea = 0

        for i in heights:
            area = (r - l) * (min(heights[r], heights[l]))
            maxarea = max(maxarea, area)

            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return maxarea