class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        uniqueNums = set(nums)

        result = 1
        while uniqueNums:
            num = min(uniqueNums)
            temp = 1

            while num + 1 in uniqueNums:
                temp += 1
                uniqueNums.remove(num)
                num += 1
            else:
                uniqueNums.remove(num)

            if temp > result:
                result = temp

            temp = 1
    
        return result