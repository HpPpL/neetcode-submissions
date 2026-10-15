class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2
            value = nums[mid]
            
            if value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
            else:
                return mid
        
        return -1 
            