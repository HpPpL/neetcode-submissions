# O(n) - time. O(n) - space.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result, stack = [0] * n, []

        for i in range(n):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)

        return result