class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sorted_h = sorted(happiness, reverse=True)
        total = 0
        for i in range(k):
            val = sorted_h[i] - i
            if val > 0:
                total += val
        return total