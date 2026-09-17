class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)

        
        result = []
        lastSeen = nums[0]
        for index, num in enumerate(nums):
            if lastSeen == num and index != 0:
                continue

            lastSeen = num
            triplets = self.twoSum(nums[min(index+1, n):], -num)
            result += triplets
            

        return result

    def twoSum(self, nums: List[int], target) -> list[List[int]]:
        result = []
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                if result and nums[left] == result[-1][1] and nums[right] == result[-1][2]:
                    pass
                else:
                    result.append([-target, nums[left], nums[right]])
                right -= 1
        
        return result

