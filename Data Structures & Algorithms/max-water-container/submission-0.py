class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:

            current_height = min(heights[left], heights[right])
            width = right - left
            current_area = current_height * width

            max_area = max(max_area, current_area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1
        
        return max_area