class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 0
        n = len(prices)
        while r < n:
            diff = prices[r] - prices[l]
            if  diff < 0:
                l = r
            else:
                if diff > profit:
                    profit = diff
                r += 1
        return profit 