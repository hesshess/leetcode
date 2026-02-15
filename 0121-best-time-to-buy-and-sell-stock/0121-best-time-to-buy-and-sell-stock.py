class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = prices[0]
        profit = 0

        for x in prices:
            if x < price:
                price = x
            else:
                if profit < (x - price):
                    profit = x - price
        return profit