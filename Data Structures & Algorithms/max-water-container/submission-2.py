class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_water = 0

        left = 0
        rigth = len(heights) - 1

        while left < rigth:

            area = (rigth - left) * min(heights[left], heights[rigth])
            max_water = max(area, max_water)

            if heights[left] <= heights[rigth]:
                left += 1
            
            else:
                rigth -= 1

        return max_water
