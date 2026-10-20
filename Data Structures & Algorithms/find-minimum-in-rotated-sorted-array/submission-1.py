# O(log(n)) - time. O(1) - space.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]


        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[0] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return nums[left]


# Idea:
# If the array is rotated (by a non-zero amount), the minimum splits it into two sorted parts:
#   left part  — from nums[0] up to the element before the minimum,
#   right part — from the minimum up to nums[-1].
# Every element of the left part is greater than every element of the right part:
#   the smallest value in the left part is nums[0],
#   the largest value in the right part is nums[-1].
# So the minimum is the first element that is smaller than nums[0].
# Edge case: if nums[0] < nums[-1], the array is not rotated and the answer is nums[0].