# O(n) - time. O(1) - space.
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, countsS1 = len(s1), Counter(s1)
        countsSubstr = Counter(s2[:n-1])
        right = n - 1
        
        while right < len(s2):
            left = right - n + 1
            countsSubstr[s2[right]] += 1
            if countsSubstr == countsS1:
                return True

            countsSubstr[s2[left]] -= 1
            if countsSubstr[s2[left]] == 0:
                del countsSubstr[s2[left]]
            
            right += 1

        return False