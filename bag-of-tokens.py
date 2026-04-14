from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = max_score = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                if score > max_score:
                    max_score = score
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return max_score
