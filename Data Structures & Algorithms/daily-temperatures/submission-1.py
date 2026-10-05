# O(n) - time. O(n) - space.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            newDay = (index, temperature)

            while len(stack) > 0 and newDay[1] > stack[-1][1]:
                passedDays = index - stack[-1][0]
                result[stack[-1][0]] = passedDays
                stack.pop()
            
            stack.append(newDay)

        return result