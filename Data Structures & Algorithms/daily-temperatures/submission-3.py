# O(n) - time. O(n) - space.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result, stack = [0] * n, []

        for i in range(n):
            while stack and temperatures[i] > temperatures[j := stack[-1]]:
                result[j] = i - j
                stack.pop()
            
            stack.append(i)

        return result