# O(n) - time. O(n) - space
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        heights.append(0) # for collapsing stack at the end.
        n = len(heights)

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                height = heights[index]
                rightArea = (i - index) * height
                
                # for repeated heights right area for leftest one.
                if stack:
                    leftBorderIndex = stack[-1]
                else:
                    leftBorderIndex = -1
                leftArea = (index - leftBorderIndex - 1) * height

                area = rightArea + leftArea
                maxArea = max(maxArea, area)

            stack.append(i)
        
        return maxArea
        