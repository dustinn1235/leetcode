# keep track of min price and update max profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        res = 0

        for price in prices:
            minPrice = min(minPrice,price)
            res = max(res, price - minPrice)
        return res