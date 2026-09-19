class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        currentLeft, currentRight = left, right

        while currentLeft < currentRight:
            print(left, right)
            currentArea = self.solveArea(heights, currentLeft, currentRight)
            if currentArea > self.solveArea(heights, left, right):
                left, right = currentLeft, currentRight

            if heights[currentLeft] <= heights[currentRight]:
                currentLeft += 1
            else:
                currentRight -= 1

        return self.solveArea(heights, left, right)


    def solveArea(self, heights: List[int], indexLeft: int, indexRight: int) -> int:
        return (indexRight - indexLeft) * min(heights[indexLeft] , heights[indexRight])
        