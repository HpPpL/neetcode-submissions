from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)

        for number, amount in count.items():
            buckets[amount].append(number)
        
        cleanBuckets = [bucket for bucket in buckets if bucket != []]
        result = []
        tmp = 0
        for cleanBucket in cleanBuckets[::-1]:
            for item in cleanBucket:
                if tmp == k:
                    return result
                else:
                    result.append(item)
                    tmp += 1

        return result