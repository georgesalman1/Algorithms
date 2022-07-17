def maxArea(height):
        l = 0
        r = len(height) -1
        area = 0
        while l < r:
            # Calculating the max area
            area = max(area, min(height[l],  height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area




height = [1,1]
print(maxArea(height))
        
        