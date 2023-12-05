class Solution(object):
    def maxArea(self, height):
        max_water = 0
        l = 0
        r = len(height) - 1

        while l < r:
            current_water = min(height[l], height[r]) * (r - l)
            max_water = max(max_water,current_water)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_water
        