from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        for c in costs:
            freq[c] += 1
        count = 0
        for price in range(1, max_cost + 1):
            if freq[price] == 0:
                continue
            if coins < price:
                break
            can_buy = min(freq[price], coins // price)
            coins -= can_buy * price
            count += can_buy
        return count
