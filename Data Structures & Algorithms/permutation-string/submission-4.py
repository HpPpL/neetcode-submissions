# O(n) - time. O(1) - space.
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, counts = len(s1), Counter(s1)
        
        for i in range(0, len(s2) - n + 1):
            if Counter(s2[i:i+n]) == counts:
                return True

        return False