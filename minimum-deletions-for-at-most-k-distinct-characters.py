class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        from collections import Counter
        freq = Counter(s)
        if len(freq) <= k:
            return 0
        counts = sorted(freq.values(), reverse=True)
        return sum(counts[k:])