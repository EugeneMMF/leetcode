class Solution:
    def maxProfit(self, inventory, orders):
        MOD = 10**9 + 7
        inventory.sort(reverse=True)
        inventory.append(0)
        profit = 0
        i = 0
        n = len(inventory)
        while orders > 0:
            cur = inventory[i]
            nxt = inventory[i + 1]
            cnt = i + 1
            diff = cur - nxt
            total = diff * cnt
            if orders >= total:
                profit += cnt * (cur + nxt + 1) * diff // 2
                orders -= total
            else:
                full = orders // cnt
                rem = orders % cnt
                low = cur - full
                profit += cnt * (cur + low + 1) * full // 2
                profit += rem * (low)
                orders = 0
            profit %= MOD
            i += 1
        return profit % MOD
