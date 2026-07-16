class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = -1
        best = 0

        for i in range(len(prices)):
            r += 1
            if prices[r] > prices[l]:
                best = max(prices[r] - prices[l], best)
            else:
                l = r
        return best
            
                