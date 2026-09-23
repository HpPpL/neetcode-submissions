class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minIndex, maxProfit = 0, 0

        for i in range(1, n):
            if maxProfit < prices[i] - prices[minIndex]:
                maxProfit = prices[i] - prices[minIndex]

            if prices[i] < prices[minIndex]:
                minIndex = i 

            print(i, minIndex, maxProfit)

        return maxProfit
