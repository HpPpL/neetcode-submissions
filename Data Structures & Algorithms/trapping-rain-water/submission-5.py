# O(n) - time. O(1) - space
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMaxHeight, rightMaxHeight = -1, -1 
        left, right = 1, n - 2
        result = 0

        while left <= right:
            leftMaxHeight = max(leftMaxHeight, height[left-1])
            rightMaxHeight = max(rightMaxHeight, height[right+1])
            
            if leftMaxHeight <= rightMaxHeight:
                result += max(0, leftMaxHeight - height[left])
                left += 1
            else:
                result += max(0, rightMaxHeight - height[right])
                right -= 1

        return result
