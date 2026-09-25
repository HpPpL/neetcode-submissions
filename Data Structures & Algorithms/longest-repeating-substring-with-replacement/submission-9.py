# O(n) - time. O(m) - space.
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letterCounter = defaultdict(int)
        left = result = 0

        for right in range(len(s)):
            letterCounter[s[right]] += 1
            windowLength = right + 1 - left

            while windowLength - max(letterCounter.values()) > k:
                letterCounter[s[left]] -= 1
                left += 1
                windowLength -= 1

            result = max(result, windowLength)

        return result            

