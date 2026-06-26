class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        chosen = set()
        x = 1
        while len(chosen) < n:
            if (k - x) not in chosen:
                chosen.add(x)
            x += 1
        return sum(chosen)
