class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        result = 0

        for num in uniqueNums:
            if num - 1 not in uniqueNums: # Значит начало последовательности потенциально
                maxLength = 1
                while num + maxLength in uniqueNums:
                    maxLength += 1
                result = max(result, maxLength)
        
        return result
