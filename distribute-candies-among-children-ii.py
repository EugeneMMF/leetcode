class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        L = limit + 1
        def comb2(k: int) -> int:
            return k * (k - 1) // 2 if k >= 2 else 0
        total = comb2(n + 2)
        total -= 3 * comb2(n - L + 2)
        total += 3 * comb2(n - 2 * L + 2)
        total -= comb2(n - 3 * L + 2)
        return total