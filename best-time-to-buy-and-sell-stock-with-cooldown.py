class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        buy_curr = -prices[0]
        sell_curr = -float('inf') 
        rest_curr = 0

        for i in range(1, n):
            buy_prev = buy_curr
            sell_prev = sell_curr
            rest_prev = rest_curr

            buy_curr = max(buy_prev, rest_prev - prices[i])

            sell_curr = buy_prev + prices[i]

            rest_curr = max(rest_prev, sell_prev)
        
        return max(sell_curr, rest_curr)
