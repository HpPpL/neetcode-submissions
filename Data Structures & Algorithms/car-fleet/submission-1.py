# O(nlogn) - time. O(n) - space.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        groupCount = 0
        n = len(position)

        for i in range(n):
            stack.append((position[i], (target - position[i]) / speed[i]))
        stack.sort(key=lambda x: x[0])
        
        while stack:
            groupLeader = stack.pop()
            leaderFinishTime = groupLeader[1]
            groupCount += 1

            while stack and stack[-1][1] <= leaderFinishTime:
                stack.pop()

        return groupCount