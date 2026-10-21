# O(log(n)) - time. O(1) - space.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Find sorted parted (at least one exsist)
            # idea of 1 place in array, where nums[i] < nums[i+1]
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    result = self.binSearch(nums[left:mid+1], target)
                    return -1 if result == -1 else result + left
                else:
                    left = mid + 1

            else:
                if nums[mid] <= target <= nums[right]:
                    result = self.binSearch(nums[mid:right+1], target)
                    return -1 if result == -1 else result + mid
                else:
                    right = mid - 1
            
        return -1   

    def binSearch(self, nums: List[int], target: int) -> int:
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
                

# Alternative ideas (both O(log n) time, O(1) space):
#
# 1. Two sorted parts.
#    Find the rotation point k (index of the minimum) with a binary search,
#    as in "Find Minimum in Rotated Sorted Array".
#    The array then splits into two sorted parts: nums[0 .. k-1] and nums[k .. n-1].
#    Compare target with nums[-1] to choose the part (target <= nums[-1] → right part),
#    then run an ordinary binary search inside it.
#
# 2. Shifted indices.
#    Find the rotation point k the same way.
#    Pretend the array is not rotated: run an ordinary binary search
#    over virtual indices 0 .. n-1, and read each element as nums[(mid + k) % n].
#    left, right and mid stay in virtual coordinates; % n is applied
#    only when reading from the array.