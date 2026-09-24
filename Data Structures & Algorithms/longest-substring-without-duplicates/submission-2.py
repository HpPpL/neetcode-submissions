# O(n) - time. O(m) - space.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left, best = 0, 0

        for right, symbol in enumerate(s):
            while symbol in window:
                window.remove(s[left])
                left += 1
            
            window.add(symbol)
            best = max(best, right - left + 1)

        return best
