
class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType)
        max_eat_count = n // 2
        unique_types_count = len(set(candyType))
        return min(unique_types_count, max_eat_count)
