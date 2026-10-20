# O(nlog(m)) - time. O(1) - space.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBananas = max(piles)
        left, right = 1, maxBananas

        while left <= right:
            mid = (left + right) // 2
            needTime = sum( -(-pile // mid) for pile in piles)

            if needTime > h:
                left = mid + 1
            else:
                right = mid - 1

        return right + 1