class Solution:
    def maxCoins(self, piles):
        n = len(piles) // 3
        piles.sort(reverse=True)
        return sum(piles[i] for i in range(1, 2 * n, 2))
