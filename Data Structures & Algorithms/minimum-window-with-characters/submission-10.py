# O(n + m) - time. O(k) - space.
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        substrCount = Counter()
        have, need = 0, len(tCount)
        left = -1
        best = (0, 0)

        for right, ch in enumerate(s):
            if tCount[ch] != 0:
                substrCount[ch] += 1

                if left == -1:
                    left = right

                if substrCount[ch] == tCount[ch]:
                    have += 1
                
                if have == need:
                    while left <= right:
                        if tCount[s[left]] != 0:
                            substrCount[s[left]] -= 1
                            if substrCount[s[left]] < tCount[s[left]]:
                                length = right + 1 - left
                                
                                if best[1] == 0 or length < best[1]:
                                    best = (left, length)
                                
                                have -= 1
                                left += 1
                                break
                        
                        left += 1 
        
        start, length = best
        return s[start:start+length]
            
        