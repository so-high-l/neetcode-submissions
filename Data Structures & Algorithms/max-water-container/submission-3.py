class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        best_area = float('-inf')

        while(left < right):
        
            width = right - left
            height_of_container = min(heights[left], heights[right])
            current_area = width * height_of_container
            best_area = max(current_area, best_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1 

        return best_area