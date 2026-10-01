# O(n) - time. O(k) - space.
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        result = []
        for index, element in enumerate(nums):
            if len(d) > 0 and index - d[0][0] >= k:
                d.popleft()

            while len(d) > 0 and d[-1][1] <= element:
                d.pop()

            d.append([index, element])
            if index >= k -1:
                result.append(d[0][1])
        
        return result