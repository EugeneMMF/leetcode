from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        best_score = -1
        best_div = None
        for d in divisors:
            score = 0
            for n in nums:
                if n % d == 0:
                    score += 1
            if score > best_score or (score == best_score and (best_div is None or d < best_div)):
                best_score = score
                best_div = d
        return best_div
