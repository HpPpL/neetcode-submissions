# O(n) - time. O(m) - space
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letterCounter = defaultdict(int)
        n = len(s)
        left = 0
        result = 0

        for right in range(n):
            letterCounter[s[right]] += 1
            currentReplaces = right + 1 - left - max(letterCounter.values(), default=0)
            
            if currentReplaces > k:
                result = max(result, len(s[left:right]))
                while currentReplaces > k:
                    letterCounter[s[left]] -= 1
                    left += 1
                    currentReplaces = right + 1 - left - max(letterCounter.values(), default=0)
        
        result = max(result, len(s[left:n]))
        return result            

