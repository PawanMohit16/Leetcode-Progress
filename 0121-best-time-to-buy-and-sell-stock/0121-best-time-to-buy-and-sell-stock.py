class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minie = prices[0]
        maxie = prices[0]
        maxprofit = 0

        n = len(prices)

        for i in range(1, n):
            maxie = max(maxie, prices[i])
            if  prices[i] < minie:
                minie = prices[i]
                maxie = prices[i]
                
            maxprofit = max(maxprofit, maxie-minie)

        return maxprofit 
            
