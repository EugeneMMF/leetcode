from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        max_a = max_b = max_c = 0
        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                if a > max_a: max_a = a
                if b > max_b: max_b = b
                if c > max_c: max_c = c
                if max_a == x and max_b == y and max_c == z:
                    return True
        return max_a == x and max_b == y and max_c == z