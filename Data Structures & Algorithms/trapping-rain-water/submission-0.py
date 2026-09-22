class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMaxHeight, rightMaxHeight = [0] * n, [0] * n

        for i in range(1, n):
            leftMaxHeight[i] = max(leftMaxHeight[i-1], height[i-1])
            rightMaxHeight[n-1-i] = max(rightMaxHeight[n-i], height[n-i])
        
        # print(height, leftMaxHeight, rightMaxHeight, sep = '\n')
        result = 0
        for i, tall in enumerate(height):
            # print(leftMaxHeight[i], rightMaxHeight[i], tall)
            result += max(0, min(leftMaxHeight[i], rightMaxHeight[i]) - tall)

        return result
