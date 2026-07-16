class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        maxprofit = 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit)
        return maxprofit