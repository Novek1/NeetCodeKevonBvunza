class Solution:
    def maxArea(self, heights: List[int]) -> int:

        areas : list = []
        left = 0
        right = len(heights) - 1
        while left < right :
            area = (right - left) * min(heights[right], heights[left])
            areas.append(area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            elif heights[left] == heights[right]:
                left += 1
                right -= 1
        return max(areas)   
            
            

