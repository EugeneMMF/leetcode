from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last = {}
        ans = float('inf')
        for i, val in enumerate(cards):
            if val in last:
                ans = min(ans, i - last[val] + 1)
            last[val] = i
        return -1 if ans == float('inf') else ans