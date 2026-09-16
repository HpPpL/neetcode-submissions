class Solution:
    def isPalindrome(self, s: str) -> bool:
        symbs = [x.lower() for x in s if x.isalnum()]
        return symbs == symbs[::-1]