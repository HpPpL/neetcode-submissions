from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)

        for number, amount in count.items():
            buckets[amount].append(number)
        
        result = []
        for bucket in reversed(buckets):
            for number in bucket:
                result.append(number)
                if len(result) == k:
                    return result