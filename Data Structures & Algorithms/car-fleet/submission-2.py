# O(nlogn) - time. O(n) - space.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        groupCount = 0
        n = len(position)

        for p, s in zip(position, speed):
            stack.append((p, (target - p) / s))
        stack.sort()
        
        while stack:
            _, leaderFinishTime = stack.pop()
            groupCount += 1

            while stack and stack[-1][1] <= leaderFinishTime:
                stack.pop()

        return groupCount