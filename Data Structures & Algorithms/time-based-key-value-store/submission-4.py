# Time: O(1) - set(), O(log(n)) - get().
# Space: O(m * n) - where n is the total number of values associated with a key, and m is the total number of keys.

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        pairs = self.timeMap[key]
        left, right = 0, len(pairs) - 1

        while left < right:
            mid = (left + right + 1) // 2
            value, time = pairs[mid]

            if time == timestamp:
                return value

            if time > timestamp:
                right = mid - 1
            else:
                left = mid
        
        return pairs[left][0] if timestamp >= pairs[left][1] else ""