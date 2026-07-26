class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)
        odd_max = 0
        even_min = float('inf')
        for f in freq.values():
            if f % 2:
                if f > odd_max:
                    odd_max = f
            else:
                if f < even_min:
                    even_min = f
        return odd_max - even_min
