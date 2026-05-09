class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        import heapq
        MOD = 10**9 + 7
        buy = []  # max-heap by negative price
        sell = []  # min-heap by price
        for price, amount, orderType in orders:
            if orderType == 0:  # buy
                while amount > 0 and sell and sell[0][0] <= price:
                    sp, sa = heapq.heappop(sell)
                    if sa > amount:
                        sa -= amount
                        heapq.heappush(sell, (sp, sa))
                        amount = 0
                    else:
                        amount -= sa
                if amount > 0:
                    heapq.heappush(buy, (-price, amount))
            else:  # sell
                while amount > 0 and buy and -buy[0][0] >= price:
                    bp, ba = heapq.heappop(buy)
                    bp = -bp
                    if ba > amount:
                        ba -= amount
                        heapq.heappush(buy, (-bp, ba))
                        amount = 0
                    else:
                        amount -= ba
                if amount > 0:
                    heapq.heappush(sell, (price, amount))
        total = 0
        for _, a in buy:
            total = (total + a) % MOD
        for _, a in sell:
            total = (total + a) % MOD
        return total