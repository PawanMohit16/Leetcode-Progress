class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        maxie = 0

        for high in range(len(prices)):
            maxie = max(maxie, prices[high] - prices[low])
            if prices[high] < prices[low]:
                low = high
        return maxie 