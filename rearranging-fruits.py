from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt1 = Counter(basket1)
        cnt2 = Counter(basket2)
        all_vals = set(cnt1.keys()).union(cnt2.keys())
        min_global = min(min(cnt1.keys(), default=10**10), min(cnt2.keys(), default=10**10))
        surplus = []
        deficit = []
        for v in all_vals:
            diff = cnt1.get(v, 0) - cnt2.get(v, 0)
            if diff % 2 != 0:
                return -1
            if diff > 0:
                surplus.extend([v] * (diff // 2))
            elif diff < 0:
                deficit.extend([v] * ((-diff) // 2))
        surplus.sort(reverse=True)
        deficit.sort()
        total_cost = 0
        for s, d in zip(surplus, deficit):
            total_cost += min(s, d, 2 * min_global)
        return total_cost
