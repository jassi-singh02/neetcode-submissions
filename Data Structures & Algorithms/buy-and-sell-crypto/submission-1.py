class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]

            if maxProfit < (prices[i] - minPrice):
                maxProfit = (prices[i] - minPrice)

        return maxProfit