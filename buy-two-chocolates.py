class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        best = -1
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                s = prices[i] + prices[j]
                if s <= money:
                    leftover = money - s
                    if leftover > best:
                        best = leftover
        return best if best != -1 else money