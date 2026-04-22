from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        window = n - k
        cur = sum(cardPoints[:window])
        min_sum = cur
        for i in range(window, n):
            cur += cardPoints[i] - cardPoints[i - window]
            if cur < min_sum:
                min_sum = cur
        return sum(cardPoints) - min_sum
