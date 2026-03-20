class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)

        if n == 0 or k == 0:
            return 0

        # If k is very large (effectively unbounded), we can make as many transactions as possible.
        # This simplifies to the "Best Time to Buy and Sell Stock II" problem,
        # where we sum all positive price differences.
        # k >= n // 2 is a common heuristic for this, as in the worst case
        # (e.g., prices = [1, 2, 1, 2, ...]), we need n // 2 transactions
        # to capture all possible profits.
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    max_profit += prices[i] - prices[i-1]
            return max_profit

        # Dynamic programming approach for limited k transactions.
        # We maintain two arrays:
        # buy[j] represents the maximum profit after completing j buys, currently holding a stock.
        # sell[j] represents the maximum profit after completing j sells, currently not holding a stock.

        # Initialize buy states to negative infinity, as we cannot have profit initially if holding a stock.
        # Initialize sell states to 0, representing no profit with 0 completed transactions.
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)

        # Iterate through each price in the given prices array
        for price in prices:
            # Iterate for transaction count 'j' from k down to 1.
            # This reverse order ensures that when calculating buy[j], sell[j-1] refers to the
            # state from the previous day's prices (before any updates for the current price).
            # Similarly, when calculating sell[j], buy[j] refers to the state after potentially
            # buying at the current price.
            for j in range(k, 0, -1):
                # Option 1: Do not buy today. Keep previous buy[j] profit.
                # Option 2: Buy today. Profit comes from (profit after j-1 sells) - current price.
                buy[j] = max(buy[j], sell[j-1] - price)
                
                # Option 1: Do not sell today. Keep previous sell[j] profit.
                # Option 2: Sell today. Profit comes from (profit after j buys, currently holding) + current price.
                sell[j] = max(sell[j], buy[j] + price)
        
        # The maximum profit will be the maximum value in the sell array,
        # as we want to end up not holding any stock to realize profit.
        return max(sell)

