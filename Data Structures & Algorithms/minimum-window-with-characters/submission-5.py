from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        substrCount = Counter()
        left, right = -1, 0
        n = len(s)
        result = ""

        while right < n:
            if tCount[s[right]] != 0:
                substrCount[s[right]] += 1
                if left == -1:
                    left = right
               
                if substrCount[s[right]] == tCount[s[right]]:
                    if tCount <= substrCount:
                        while left <= right:
                            if right + 1 - left < len(result) or result == "":
                                result = s[left:right+1]

                            if tCount[s[left]] != 0:
                                substrCount[s[left]] -= 1
                            left += 1
                            
                            if substrCount[s[left-1]] < tCount[s[left-1]]:
                                break

            right += 1

        return result