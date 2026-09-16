class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start, end = 0, len(s) - 1

        while start < end:
            print(start, end)
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start] == s[end]:
                start += 1
                end -= 1
                continue
            else:
                return False
        else:
            return True