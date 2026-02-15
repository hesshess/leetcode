class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_p = 0
        for x in prices:
            if x < buy:
                buy = x
                print('buy:,',buy)
            if max_p < (x - buy):
                max_p = x - buy
            print('max_p:', max_p)
        return max_p
