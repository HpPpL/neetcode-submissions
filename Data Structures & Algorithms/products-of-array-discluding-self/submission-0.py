from itertools import accumulate
import operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = list(accumulate(nums, operator.mul))
        postfix = list(accumulate(nums[::-1], operator.mul))
        postfix = postfix[::-1]
        
        result = [0 for i in range(n)]
        result[0] = postfix[1]
        result[n-1] = prefix[n-2]
        
        for i in range(1, n-1):
            result[i] = prefix[i-1] * postfix[i+1]

        return result
