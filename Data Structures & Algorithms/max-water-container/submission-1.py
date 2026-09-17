class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n < 2: return 0
        left, right = 0, n - 1
        def area(): 
            return min(heights[left], heights[right]) * (right - left) 
        maxArea = area()
        while left < right:
            if area() > maxArea:
                maxArea = area()
            if heights[right] > heights[left]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -=1
        return maxArea

                    


        