from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [numbers for numbers, _ in Counter(nums).most_common(k)]