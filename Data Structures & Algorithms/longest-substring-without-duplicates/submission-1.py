class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        startSubstringIndex = 0
        symbSet = set()
        maxLengthSubstring = 0

        for i in range(len(s)):
            currentLength = len(symbSet)
            symbSet.add(s[i])

            if len(symbSet) == currentLength: # Встретили повтор
                maxLengthSubstring = max(maxLengthSubstring, len(symbSet))
                while startSubstringIndex < i:
                    if s[startSubstringIndex] == s[i]: ## Нашли повтор символ
                        startSubstringIndex += 1
                        break
                    # Повтора в данной позиции нет - двигаемся дальше
                    symbSet.remove(s[startSubstringIndex]) # Дропаем встретившийся символ
                    startSubstringIndex += 1


        maxLengthSubstring = max(maxLengthSubstring, len(symbSet))
        return maxLengthSubstring
